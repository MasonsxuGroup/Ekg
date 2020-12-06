import os
from threading import main_thread
import pandas as pd
from tqdm.std import trange


def check_data(folderpath_origin, folderpath_dest):
    """处理因人工标注造成的字符合并问题（单个文件）

    Args:
        : folderpath_origin(str): Folder，待处理文件路径
        : folderpath_dest(str): Folder，已处理数据保存路径
    """

    all_data = pd.read_csv(folderpath_origin, header=None)
    all_data = all_data.values.tolist()
    new_all_data_list = []
    for data_index in trange(len(all_data)):
        data = all_data[data_index]
        if (str(data[0]) != 'nan') and (not str(data[0]).isdigit()) and (len(data[0]) > 1):
            for i in range(len(data[0])):
                new_data_list = []
                new_data_list.append(data[0][i])
                new_data_list.append('O')
                new_all_data_list.append(new_data_list)
        else:
            new_all_data_list.append(data)

    sheet = pd.DataFrame(new_all_data_list)
    filename = folderpath_dest
    sheet.to_csv(filename, index=None, header=None)


def check_datas(folderpath_origin, folderpath_dest):
    """处理因人工标注造成的字符合并问题（多个文件处于同一目录下）

    Args:
        : folderpath_origin(str): Folder，待处理文件目录路径
        : folderpath_dest(str): Folder，已处理数据保存目录路径
    """

    filenames = os.listdir(folderpath_origin)

    for filename in filenames:
        if len(filename) == 13:
            filename = folderpath_origin + filename
            print(filename)
            all_data = pd.read_csv(filename, header=None)
            all_data = all_data.values.tolist()
            new_all_data_list = []
            for data_index in trange(len(all_data)):
                data = all_data[data_index]
                if (str(data[0]) != 'nan') and (not str(data[0]).isdigit()) and (len(data[0]) > 1):
                    for i in range(len(data[0])):
                        new_data_list = []
                        new_data_list.append(data[0][i])
                        new_data_list.append('O')
                        new_all_data_list.append(new_data_list)
                else:
                    new_all_data_list.append(data)
            sheet = pd.DataFrame(new_all_data_list)
            filename = folderpath_dest + 'G_' + filename[-13:]
            sheet.to_csv(filename, index=None, header=None)


if __name__ == '__main__':
    # check_datas('Data_Pre/Marked_Data/', 'Data_Pre/Marked_Data/')
    check_data('Data_Pre/Extract_Data_Pre/all_extract_part_4.txt',
               '/Users/macx/Desktop/all_extract_part_4.txt')
