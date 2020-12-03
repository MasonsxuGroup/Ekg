import os
import ssl
import json
import time
import pandas as pd
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from tqdm.std import trange

# skip https auth
ssl._create_default_https_context = ssl._create_unverified_context

API_KEY = 'jm5tBpX9Zrx3xtyjIylCjhzl'

SECRET_KEY = 'cQGoLhMRsLAvl5utOrpRco35wSj7w70G'

COMMENT_TAG_URL = "https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer"

"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'


def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    result_str = ''
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    result_str = result_str.decode()

    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print('please overwrite the correct API_KEY and SECRET_KEY')
        exit()


def make_request(url, comment_list):
    new_data = {}  # 存放当前数据中实体的提取结果
    res_data_list = []  # 存放数据中的所有 res 实体
    res_data_dict = {}  # 存放数据中的单个 res 实体
    for comment in comment_list:
        response = request(url, json.dumps(
            {
                "text": comment + '。',
            }))
        data = json.loads(response)
        if "error_code" not in data or data["error_code"] == 0:
            for item in data["items"]:
                if str(item["ne"]).isupper():
                    res_data_dict['marker'] = item['ne']
                    res_data_dict['item'] = item['item']
                    res_data_list.append(res_data_dict)
                    res_data_dict = {}
                elif item['pos'] == 'v' or item['pos'] == 'vn' or item['pos'] == 'n' or item['pos'] == 'm':
                    res_data_dict['marker'] = 'RES'
                    res_data_dict['item'] = item['item']
                    res_data_list.append(res_data_dict)
                    res_data_dict = {}
                else:
                    res_data_dict['marker'] = 'O'
                    res_data_dict['item'] = item['item']
                    res_data_list.append(res_data_dict)
                    res_data_dict = {}
        else:
            print(response)
        time.sleep(0.5)  # 防止qps超限
    new_data['data'] = res_data_list
    return new_data


def request(url, data):
    req = Request(url, data.encode('utf-8'))
    try:
        f = urlopen(req)
        result_str = f.read()
        result_str = result_str.decode()
        return result_str
    except URLError as err:
        print(err)


def get_data(folderpath_origin):
    filename = os.listdir(folderpath_origin)
    all_data = []
    punc = '　# '
    trans = str.maketrans({key: None for key in punc})
    for name in filename:
        path = folderpath_origin + name
        if path[-5:] == '.xlsx':
            data = pd.read_excel(path)
            abstracts = data['摘要'].to_list()
            for abstract in abstracts:
                abstract = str(abstract).translate(trans).replace('\u200b', '')
                all_data.append(abstract)
        elif path[-4:] == '.csv':
            data = pd.read_csv(path)
            detaileds = data['详细'].to_list()
            for detailed in detaileds:
                detailed = str(detailed).translate(trans).replace('\u200b', '')
                all_data.append(detailed)
    new_all_data = []
    print('开始去重处理！！！')
    for data_index in trange(len(all_data)):
        data = all_data[data_index]
        if data not in new_all_data:
            new_all_data.append(data)
    return new_all_data


def tq_data(url, all_data):
    all_data_length = len(all_data)
    all_pre_data = []
    for index in trange(all_data_length):
        now_data = all_data[index]
        now_data_list = list(filter(None, now_data.split('。')))
        pre_data = make_request(url, now_data_list)
        all_pre_data.append(pre_data)
    return all_pre_data


def save_all_data(all_pre_data, folderpath_dest):
    sheet = pd.DataFrame(all_pre_data)
    filename = folderpath_dest + 'Emergencies_All_Data.json'
    sheet.to_json(filename, force_ascii=False)


def run(folderpath_origin, folderpath_dest):
    token = fetch_token()
    url = COMMENT_TAG_URL + "?charset=UTF-8&access_token=" + token
    all_data = get_data(folderpath_origin)
    print('数据加载完毕')
    all_pre_data = tq_data(url, all_data)
    print('已成功提取所有实体')
    save_all_data(all_pre_data, folderpath_dest)
    print('提取的所有数据已保存为 json 文件')


if __name__ == '__main__':
    News_Data_Origin_Path = 'Data_Pre/News_Data_Origin/'
    Emergencies_Data_Path = 'Data_Pre/Emergencies_Data_Pre/'
    run(News_Data_Origin_Path, Emergencies_Data_Path)
