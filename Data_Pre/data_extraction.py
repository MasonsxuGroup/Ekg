import pandas as pd
from tqdm.std import trange


def merge_data(all_data):
    """合并标记数据（B、I）

    Args:
        :all_data (list): list of data，加载的所有标记数据列表，包含B、I
    """

    Merged_Data_List = []  # 存放所有实体字典
    print('开始合并所有邻近标记的实体：')
    for data_index in trange(len(all_data['data'])):
        data = all_data['data'][data_index]
        item = ''
        data_length = len(data)
        Merged_Data_Dict = {}  # 存放合并后的所有实体对
        merged_data_list = []  # 存放合并后的实体字典
        merged_data_dict = {}  # 存放合并后的实体对象
        for index in range(data_length):
            if index == data_length - 1:
                if item == '':
                    merged_data_dict['item'] = data[index]['item']
                    merged_data_dict['marker'] = data[index]['marker']
                    merged_data_list.append(merged_data_dict)
                    merged_data_dict = {}
                else:
                    item += data[index]['item']
                    merged_data_dict['item'] = item
                    merged_data_dict['marker'] = data[index]['marker']
                    merged_data_list.append(merged_data_dict)
                    merged_data_dict = {}
                    item = ''
            elif data[index]['marker'] == 'O':
                merged_data_dict['item'] = data[index]['item']
                merged_data_dict['marker'] = data[index]['marker']
                merged_data_list.append(merged_data_dict)
                merged_data_dict = {}
            elif data[index]['marker'] != data[index + 1]['marker'] and item == '':
                merged_data_dict['item'] = data[index]['item']
                merged_data_dict['marker'] = data[index]['marker']
                merged_data_list.append(merged_data_dict)
                merged_data_dict = {}
            elif data[index]['marker'] == data[index + 1]['marker']:
                item += data[index]['item']
            elif data[index]['marker'] != data[index + 1]['marker'] and item != '':
                item += data[index]['item']
                merged_data_dict['item'] = item
                merged_data_dict['marker'] = data[index]['marker']
                merged_data_list.append(merged_data_dict)
                merged_data_dict = {}
                item = ''
        Merged_Data_Dict['data'] = merged_data_list
        Merged_Data_List.append(Merged_Data_Dict)
    return Merged_Data_List


def marker_data(all_data):
    """转换标记，并拆分字符串

    Args:
        :all_data (dict): dictionary，加载的所有数据字典

    """
    extract_data_lists = []
    print('转换标记，并拆分字符串：')
    for item_index in trange(len(all_data['data'])):
        item = all_data['data'][item_index]
        for cell in item:
            if cell['marker'] == 'O':
                extract_data_list = []
                extract_data_list.append(cell['item'])
                extract_data_list.append(cell['marker'])
                number_data = ''
                if len(extract_data_list) == 2:
                    extract_data_lists.append(extract_data_list)
            else:
                marker_len = len(extract_data_lists)
                number_data = ''
                for index in range(0, len(cell['item'])):  # 拆分字符串，并合并字符串中的数字
                    extract_data_list = []
                    # 判断是否为字符串的开始 index，并设置长度避免超出字符串 index
                    if (str(cell['item'][index]).isdigit() is False) or (index == len(cell['item']) - 1):
                        marker = 'I-' + cell['marker']
                        extract_data_list.append(cell['item'][index])
                        extract_data_list.append(marker)
                    elif (str(cell['item'][index]).isdigit()) and (str(cell['item'][index + 1]).isdigit()):
                        number_data += str(cell['item'][index])
                    elif str(cell['item'][index]).isdigit() and (str(cell['item'][index + 1]).isdigit() is False):
                        number_data += str(cell['item'][index])
                        marker = 'I-' + cell['marker']
                        extract_data_list.append(number_data)
                        extract_data_list.append(marker)
                        number_data = ''
                    if len(extract_data_list) == 2:
                        extract_data_lists.append(extract_data_list)
                extract_data_lists[marker_len][1] = 'B' + \
                    extract_data_lists[marker_len][1][1:]
        extract_data_lists.append('')
    return extract_data_lists


def save_marker_data(all_extract_data, folderpath_dest):
    """保存所有已识别的数据

    Args:
        :all_extract_data (list): list of extracted，已经标注好的数据列表
    """

    sheet = pd.DataFrame(all_extract_data)
    filename = folderpath_dest + 'all_extract_data.txt'
    sheet.to_csv(filename, index=None, header=None)


def save_merged_data(all_pre_data, folderpath_dest):
    """保存所有已识别数据字典

    Args:
        :all_pre_data (dict): dictionary，所有已识别的数据(Dict)
        :folderpath_dest (str): path of folder，已识别数据待保存文件目录的路径
    """

    sheet = pd.DataFrame(all_pre_data)
    filename = folderpath_dest + 'Emergencies_Merged_Data.json'
    sheet.to_json(filename, force_ascii=False)


def save_mean_data(data, amount, folderpath_dest):
    """将已识别的数据按照小组人数进行切分，方便后续继续进行核查

    Args:
        :data (list): list of data，所有已识别数据列表
        :amount (int): amount to people，均分的次数
        :folderpath_dest (str): path of folder，已识别数据待保存文件目录的路径
    """

    all_data_length = len(data)
    mean_data_length = all_data_length//amount
    start = 0
    end = mean_data_length
    print('开始平均所有数据')
    for index in trange(amount):
        while len(data[end - 1]) != 0:
            end += 1
        else:
            sheet = pd.DataFrame(data[start:end - 1])
            filename = folderpath_dest + 'all_extract_part_' + \
                str(index) + '.txt'
            sheet.to_csv(filename, index=None, header=None)
            start = end
            end += mean_data_length
            if end > all_data_length:
                end = all_data_length


def run(folderpath_origin, folderpath_dest):
    """启动方法

    Args:
        :folderpath_origin (str): Folder，待处理文件路径
        :folderpath_dest (str): Folder，已处理数据保存路径
    """

    Emergencies_All_Data_Path = folderpath_origin + 'Emergencies_All_Data.json'
    data = pd.read_json(Emergencies_All_Data_Path)
    merged_data_list = merge_data(data)
    save_merged_data(merged_data_list, folderpath_dest)
    Emergencies_Merged_Data_Path = folderpath_dest + 'Emergencies_Merged_Data.json'
    data = pd.read_json(Emergencies_Merged_Data_Path)
    extract_data_lists = marker_data(data)
    save_marker_data(extract_data_lists, folderpath_dest)
    save_mean_data(extract_data_lists, 5, folderpath_dest)


if __name__ == "__main__":
    folderpath_origin = 'Data_Pre/Emergencies_Data_Pre/'
    folderpath_dest = 'Data_Pre/Extract_Data_Pre/'
    run(folderpath_origin, folderpath_dest)
