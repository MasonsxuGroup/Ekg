import os
import pandas as pd
from tqdm.std import trange


def get_data(folderpath_origin):
    """加载数据

    Args:
        :folderpath_origin (str): Folder，待加载数据文件目录
    """

    filename = os.listdir(folderpath_origin)
    merged_data_list = []
    print('开始合并所有文件中的数据')
    for name_index in trange(len(filename)):
        name = filename[name_index]
        if str(name)[-5:] == 'w.txt':
            path = folderpath_origin + name
            with open(path, 'r') as f:
                for chunk in f:
                    if str(chunk)[0] != ' ':
                        merged_data_list.append(chunk)
        else:
            print('\n不是目标文件，跳过当前文件。')
    return merged_data_list


def save_merged_data(all_pre_data, folderpath_dest):
    """保存合并后的数据，并去除','、空格（行）

    Args:
        :all_pre_data (list): list of pre data，合并后的数据列表
        :folderpath_dest (str): path of folder，处理好的数据保存目录
    """

    print('开始保存所有数据')
    filename = folderpath_dest + 'all_marked_data.txt'
    with open(filename, 'w') as f:
        for data_index in trange(len(all_pre_data)):
            data = str(all_pre_data[data_index]).replace(',', ' ').replace('\n', '')
            if '。' in list(data):
                f.write(data + '\n')
                f.write('\n')
            elif (len(data) > 1) and (str(data)[0] != ' '):
                f.write(data + '\n')


def run(folderpath_origin, folderpath_dest):
    """多个标记好的文件进行合并

    Args:
        :folderpath_origin (str): Folder，待加载数据文件目录
        :folderpath_dest (str): path of folder，处理好的数据保存目录
    """

    merged_data_list = get_data(folderpath_origin)
    save_merged_data(merged_data_list, folderpath_dest)


if __name__ == "__main__":
    Extract_Data_Pre_Patch = 'Data_Pre/Marked_Data/'
    Marked_Data_Path = 'Data_Pre/Marked_Data/'
    run(Extract_Data_Pre_Patch, Marked_Data_Path)
