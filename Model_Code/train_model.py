import random
import pandas as pd
from LAC import LAC
from tqdm.std import trange


def merge_all_data(folderpath_origin, folderpath_dest):
    """ 合并所有已经标注好的数据

    Args:
        :folderpath_origin (str): Folder，已经标注好的数据文件的路径
        :folderpath_dest (str): Destination，合并后的数据将要保存的路径
    """

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
            elif (all_data[data_index + 1][1][0] == 'B') and (data[1][2:] == all_data[data_index + 1][1][2:]):
                data_str = data[0] + '/' + data[1][2:] + ' '
                f.write(data_str)
            elif (all_data[data_index + 1][1][0] != 'B') and (data[1][2:] == all_data[data_index + 1][1][2:]):
                data_str = data[0]
                f.write(data_str)
            elif data[1][2:] != all_data[data_index + 1][1][2:]:
                data_str = data[0] + '/' + data[1][2:] + ' '
                f.write(data_str)


def split_data(folderpath_dest, shuffle=False, ratio=0.2):
    """划分数据集

    划分数据集变量作用

    Args:
        :folderpath_dest (str):数据集的路径
        :shuffle (bool):是否重新排序
        :ratio (float):划分比例

    Returns:
        sublist_1 sublist_2
    """
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
    """ 保存划分后的数据

    Args:
        :sublist_1 (list): list of split，划分的测试数据集
        :sublist_2 (list): list of split，划分的训练数据集
        :folderpath_dest (str): path of folder file，文件的保存目录
    """

    filename_test = folderpath_dest + 'test.tsv'
    filename_train = folderpath_dest + 'train.tsv'
    sheet_test = pd.DataFrame(sublist_1)
    sheet_train = pd.DataFrame(sublist_2)
    sheet_test.to_csv(filename_test, index=None, header=None)
    sheet_train.to_csv(filename_train, index=None, header=None)


def save_data_dict(folderpath_dest):
    """ 保存数据字典

    Args:
        :folderpath_dest (str): folder，文件的保存目录
    """

    print('开始分割数据字典')
    filename_origin = folderpath_dest + 'all_marked_data.txt'
    data = pd.read_csv(filename_origin, header=None)
    data = data.values.tolist()
    marked_data_dict = []  # 存放标记数据的检索词
    data_dict = []  # 存放标记数据的完整数据
    for data_index in trange(len(data)):
        now_data = data[data_index][0]
        data_list = now_data.split(' ')
        for cell in data_list:
            cell_marked = str(cell).split('/')[0]
            if cell_marked not in marked_data_dict:
                marked_data_dict.append(cell_marked)
                data_dict.append(cell)
    sheet = pd.DataFrame(data_dict)
    filename_dest = folderpath_dest + 'dict.txt'
    sheet.to_csv(filename_dest, index=None, header=None)


def train_model(model_path, train_file_path, test_file_path):
    """ 训练模型

    Args:
        :model_path (str): path of model file，模型保存的目录
        :train_file_path (str): path of training file，训练数据文件保存路径
        :test_file_path (str): path of testing file，测试数据文件保存路径
    """

    # 选择使用默认的词法分析模型
    lac = LAC()
    # 训练和测试数据集，格式一致
    train_file = train_file_path
    test_file = test_file_path
    lac.train(model_save_dir=model_path,
              train_data=train_file, test_data=test_file)


def run(folderpath_origin, folderpath_dest,
        model_path, train_file_path, test_file_path):
    """ 训练模型

    Args:
        :folderpath_origin (str): Folder，待处理文件路径
        :folderpath_dest (str): Folder，已处理数据保存路径
        :model_path (str): path of model file，模型保存的目录
        :train_file_path (str): path of training file，训练数据文件保存路径
        :test_file_path (str): path of testing file，测试数据文件保存路径
    """

    merge_all_data(folderpath_origin, folderpath_dest)
    sublist_1, sublist_2 = split_data(folderpath_dest, shuffle=True, ratio=0.2)
    save_split_data(sublist_1, sublist_2, folderpath_dest)
    save_data_dict(folderpath_dest)
    train_model(folderpath_origin, folderpath_dest,
                model_path, train_file_path, test_file_path)


if __name__ == "__main__":
    folderpath_origin = 'Data_Pre/Marked_Data/'
    folderpath_dest = 'Model_Code/data/'
    model_path = 'Model_Code/model/'
    train_file_path = 'Model_Code/data/train.tsv'
    test_file_path = 'Model_Code/data/test.tsv'
    run(folderpath_origin, folderpath_dest,
        model_path, train_file_path, test_file_path)
