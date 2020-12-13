import re
import time
import pandas as pd
from tqdm.std import trange
from bs4 import BeautifulSoup
from multiprocessing import cpu_count
from multiprocessing.pool import Pool
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.chrome.service import Service

crawler_service = Service(executable_path='geckodriver',)
crawler_service.command_line_args()
crawler_service.start()
option = FirefoxOptions()
option.add_argument("--headless")  # 隐藏浏览器
browser = Firefox(options=option)


def get_title_url(url):
    href_lists = []
    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    try:
        uls = soup.find('ul', {'class': 'zxxx_list'})
        for li in uls.find_all('li'):
            a_list = []
            a_tag = li.find('a')
            a_list.append(a_tag['title'])
            a_list.append('http://www.nhc.gov.cn' + a_tag['href'])
            a_list.append(li.find('span').text)
            href_lists.append(a_list)
    except Exception as e:
        print(e)
    return href_lists


def get_news_data(title_ulr_list):
    news_list = []
    browser.get(title_ulr_list[1])
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    try:
        news_list.append(title_ulr_list[0])
        news_list.append(title_ulr_list[1])
        news_list.append(title_ulr_list[2])
        content = soup.find('div', {'class': 'con'}).text
        punc = "\n\t "  # 需要删除的特殊字符
        trans = str.maketrans({key: None for key in punc})  # 删除特殊字符
        news_list.append(
            str(content)
            .translate(trans)
            .replace('\u2002', '')
            .replace('\xa0', '')
            .replace('分享到', '')
        )
    except Exception as e:
        print(e)
    return news_list


def sand_url():
    type_lists = ['yqtb', 'fkdt', 'zhengcwj', 'yhfc']
    urls = []
    for type_index in trange(len(type_lists)):
        type = type_lists[type_index]
        url = "http://www.nhc.gov.cn/xcs/" + str(type) + "/list_gzbd.shtml"
        browser.get(url)
        time.sleep(3)
        page_tag = str(
            browser.find_elements_by_class_name('pagination_index_last').text
        )
        max_num = re.findall(".*共(.*)页.*", page_tag)
        urls.append(url)
        for page in range(2, max_num):
            url = (
                "http://www.nhc.gov.cn/xcs/"
                + str(type)
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


def save_news_data(folderpath_dest, news_data_lists):
    sheet = pd.DataFrame(news_data_lists, columns=["标题", "url", "日期", "详细"])
    filename = folderpath_dest + "/" + "新冠肺炎相关事件.csv"
    sheet.to_csv(filename, index=None)


def run(folderpath_dest):
    try:
        urls = sand_url()
        title_ulr_lists = sort_out_href(get_title_url, urls)
        news_data_lists = sort_out_news(get_news_data, title_ulr_lists)
        save_news_data(folderpath_dest, news_data_lists)
        browser.quit()
        crawler_service.stop()
    except Exception as e:
        print(e)
        browser.quit()
        crawler_service.stop()


if __name__ == '__main__':
    # folderpath_dest = 'Crawler_Job_Ekg/NHC_Data'
    # run(folderpath_dest)
    sand_url()
