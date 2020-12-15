import time
import string
import requests
import pandas as pd
from tqdm.std import trange
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from multiprocessing import cpu_count
from multiprocessing.pool import Pool
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions


def find_href(href_list):
    return len(href_list) == 3


def find_news_data(news_data_list):
    return len(news_data_list) == 4


def get_html(url, cookie=None):
    ua = UserAgent(verify_ssl=False)  # 调用UserAgent库生成ua对象
    header = {'User-Agent': ua.random, "Cookie": cookie}
    try:
        r = requests.get(url, timeout=300, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding  # 指定编码形式
        return r.text
    except:
        return "please inspect your url or setup"


def get_cookie(url):
    option = FirefoxOptions()
    option.set_preference('permissions.default.image', 2)  # 设置无图模式
    option.add_argument('--headless')  # 设置无头模式
    browser = Firefox(options=option)
    browser.get(url)
    time.sleep(5)
    Cookies = browser.get_cookies()
    browser.quit()
    cookies = ''
    # 获取cookie中的name和value,转化成requests可以使用的形式
    for cookie in Cookies:
        cookies += cookie['name'] + "=" + cookie['value'] + ";"
    return cookies


def get_title_url(url):
    global cookie
    href_lists = []
    try:
        html = get_html(url, cookie=cookie)
        soup = BeautifulSoup(html, 'lxml')
        uls = soup.find('ul', {'class': 'zxxx_list'})
        for li in uls.find_all('li'):
            a_list = []
            a_tag = li.find('a')
            a_list.append(a_tag['title'])
            if (href := a_tag['href'])[:4] != "http":
                a_list.append('http://www.nhc.gov.cn' + href)
            a_list.append(li.find('span').text)
            href_lists.append(a_list)
    except Exception as e:
        print("======>>>ERROR: 重新获取 Cookie <<<======")
        cookie = get_cookie(url)
        html = get_html(url, cookie=cookie)
        soup = BeautifulSoup(html, 'lxml')
        uls = soup.find('ul', {'class': 'zxxx_list'})
        for li in uls.find_all('li'):
            a_list = []
            a_tag = li.find('a')
            a_list.append(a_tag['title'])
            if (href := a_tag['href'])[:4] != "http":
                a_list.append('http://www.nhc.gov.cn' + href)
            a_list.append(li.find('span').text)
            href_lists.append(a_list)
    return href_lists


def get_news_data(title_ulr_list):
    global cookie
    news_list = []
    news_list.append(title_ulr_list[0])
    news_list.append(title_ulr_list[1])
    news_list.append(title_ulr_list[2])
    try:
        html = get_html(title_ulr_list[1], cookie=cookie)
        soup = BeautifulSoup(html, 'lxml')
        try:
            content = soup.find('div', {'class': 'con'}).text
            print(content.encode('utf-8'))
            punc = u' \t\n\r\x0b\x0c\xc2\xa0\u2002\u3000'
            trans = str.maketrans({key: None for key in punc})  # 删除特殊字符
            news_list.append(str(content).translate(trans).replace('分享到', ''))
        except Exception as e:
            print("======>>>跳过当前非文本页面<<<======")
    except Exception as e:
        print("======>>>ERROR: 重新获取 Cookie <<<======")
        cookie = get_cookie(title_ulr_list[1])
        html = get_html(title_ulr_list[1], cookie=cookie)
        soup = BeautifulSoup(html, 'lxml')
        try:
            content = soup.find('div', {'class': 'con'}).text
            punc = u' \t\n\r\x0b\x0c\xc2\xa0\u2002\u3000'
            trans = str.maketrans({key: None for key in punc})  # 删除特殊字符
            news_list.append(str(content).translate(trans).replace('分享到', ''))
        except Exception as e:
            print("======>>>跳过当前非文本页面<<<======")
    return news_list


def sand_url():
    section_types = pd.read_json('Crawler_Job_Ekg/config/config.json')['section_types']
    urls = []
    for section_type in section_types:
        url = (
            "http://www.nhc.gov.cn/xcs/"
            + str(section_type['type'])
            + "/list_gzbd.shtml"
        )
        urls.append(url)
        for page in range(2, int(section_type['pagination']) + 1):
            url = (
                "http://www.nhc.gov.cn/xcs/"
                + str(section_type['type'])
                + "/list_gzbd_"
                + str(page)
                + ".shtml"
            )
            urls.append(url)
    return urls


def process_pools(func, urls):
    pool = Pool(cpu_count())
    result_lists = pool.map(func, urls)
    pool.close()
    pool.join()
    return result_lists


def sort_out_href(func, urls):
    print("======>>>开始整理所有新闻的超链接地址<<<======")
    title_ulr_lists = []
    href_lists = process_pools(func, urls)
    for href_list_index in trange(len(href_lists)):
        href_list = href_lists[href_list_index]
        for href in href_list:
            title_ulr_lists.append(href)
    return title_ulr_lists


def sort_out_news(func, title_ulr_lists):
    print("======>>>开始整理所有新闻的详细信息<<<======")
    news_data_lists = []
    news_lists = process_pools(func, title_ulr_lists)
    for news_list_index in trange(len(news_lists)):
        news_data_lists.append(news_lists[news_list_index])
    return news_data_lists


def save_titles_data(folderpath_dest, title_ulr_lists):
    sheet = pd.DataFrame(title_ulr_lists, columns=["标题", "url", "日期"])
    filename = folderpath_dest + "/" + "新冠肺炎相关事件（标题）.csv"
    sheet.to_csv(filename, index=None)


def save_news_data(folderpath_dest, news_data_lists):
    sheet = pd.DataFrame(news_data_lists, columns=["标题", "url", "日期", "详细"])
    filename = folderpath_dest + "/" + "新冠肺炎相关事件（详细）.csv"
    sheet.to_csv(filename, index=None)


def run(folderpath_dest):
    try:
        urls = sand_url()
        title_ulr_lists = sort_out_href(get_title_url, urls)
        title_ulr_lists = list(filter(find_href, title_ulr_lists))
        save_titles_data(folderpath_dest, title_ulr_lists)
        news_data_lists = sort_out_news(get_news_data, title_ulr_lists)
        news_data_lists = list(filter(find_news_data, news_data_lists))
        save_news_data(folderpath_dest, news_data_lists)
    except Exception as e:
        print(e)


cookie = get_cookie("http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml")
if __name__ == '__main__':
    folderpath_dest = 'Crawler_Job_Ekg/NHC_Data'
    run(folderpath_dest)
