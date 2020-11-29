import random
import pandas as pd
from tqdm.std import trange


def merge_all_data(folderpath_origin, folderpath_dest):
    print('开始合并所有标注数据')
    all_data = []
    filename_origin = folderpath_origin + 'all_marked_data.txt'
    with open(filename_origin, 'r') as f:
        for data in f:
            if len(str(data)) > 1:
                all_data.append(data.replace('\n', '').split(' '))
    filename_dest = folderpath_dest + 'all_marked_data.txt'
    with open(filename_dest, 'w') as f:
        data_str = ''
        for data_index in trange(len(all_data)):
            data = all_data[data_index]
            if data[0] == '。' or data_index == len(all_data) - 1:
                data_str = data[0] + '/O' + '\n'
                f.write(data_str)
            elif data[1] == 'O':
                data_str = data[0] + '/O '
                f.write(data_str)
            elif data[1][2:] == all_data[data_index + 1][1][2:]:
                data_str = data[0]
                f.write(data_str)
            elif data[1][2:] != all_data[data_index + 1][1][2:]:
                data_str = data[0] + '/' + data[1][2:] + ' '
                f.write(data_str)


def split_data(folderpath_dest, shuffle=False, ratio=0.2):
    '''划分数据集

    划分数据集变量作用
    Args:
        folderpath_dest (str):数据集的路径
        shuffle (bool):是否重新排序
        ratio (float):划分比例
    Returns:
        sublist_1 sublist_2
    '''
    filename_dest = folderpath_dest + 'all_marked_data.txt'
    data = pd.read_csv(filename_dest, header=None)
    data = data.values.tolist()
    n_total = len(data)
    offset = int(n_total * ratio)
    if n_total == 0 or shuffle < 1:
        return [], data
    if shuffle:
        random.shuffle(data)
    sublist_1 = data[:offset]
    sublist_2 = data[offset:]
    return sublist_1, sublist_2


def save_split_data(sublist_1, sublist_2, folderpath_dest):
    filename_test = folderpath_dest + 'test.tsv'
    filename_train = folderpath_dest + 'train.tsv'
    sheet_test = pd.DataFrame(sublist_1)
    sheet_train = pd.DataFrame(sublist_2)
    sheet_test.to_csv(filename_test, index=None, header=None)
    sheet_train.to_csv(filename_train, index=None, header=None)


def save_data_dict(folderpath_dest):
    print('开始分割数据字典')
    filename_origin = folderpath_dest + 'all_marked_data.txt'
    data = pd.read_csv(filename_origin, header=None)
    data = data.values.tolist()
    data_dict = []
    for data_index in trange(len(data)):
        now_data = data[data_index][0]
        data_list = now_data.split(' ')
        for cell in data_list:
            if cell not in data_dict:
                data_dict.append(cell)
    sheet = pd.DataFrame(data_dict)
    filename_dest = folderpath_dest + 'dict.txt'
    sheet.to_csv(filename_dest, index=None, header=None)


def run(folderpath_origin, folderpath_dest):
    merge_all_data(folderpath_origin, folderpath_dest)
    sublist_1, sublist_2 = split_data(folderpath_dest, shuffle=True, ratio=0.2)
    save_split_data(sublist_1, sublist_2, folderpath_dest)
    save_data_dict(folderpath_dest)


if __name__ == "__main__":
    folderpath_origin = 'Data_Pre/Marked_Data/'
    folderpath_dest = 'Model_Code/data/'
    run(folderpath_origin, folderpath_dest)
