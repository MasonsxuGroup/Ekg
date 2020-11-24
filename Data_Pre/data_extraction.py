import pandas as pd


def merge_data(all_data):
    Merged_Data_List = []  # 存放所有实体字典
    for data in all_data['data']:
        item = ''
        data_length = len(data)
        Merged_Data_Dict = {}  # 存放合并后的所有实体对
        merged_data_list = []  # 存放合并后的实体字典
        merged_data_dict = {}  # 存放合并后的实体对象
        for index in range(0, data_length):
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
    extract_data_lists = []
    for item in all_data['data']:
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
    return extract_data_lists


def save_marker_data(all_extract_data):
    sheet = pd.DataFrame(all_extract_data)
    sheet.to_csv('./Data_Pre/config/all_extract_data.csv',
                 index=None, header=None)


def save_merged_data(all_pre_data, folderpath_dest):
    sheet = pd.DataFrame(all_pre_data)
    filename = folderpath_dest + 'Emergencies_Merged_Data.json'
    sheet.to_json(filename, force_ascii=False)


def run(folderpath_dest):
    data = pd.read_json(
        './Data_Pre/Emergencies_Data_Pre/Emergencies_All_Data.json')
    merged_data_list = merge_data(data)
    save_merged_data(merged_data_list, folderpath_dest)
    data = pd.read_json(
        './Data_Pre/Emergencies_Data_Pre/Emergencies_Merged_Data.json')
    extract_data_lists = marker_data(data)
    save_marker_data(extract_data_lists)


if __name__ == "__main__":
    Emergencies_Data_Path = 'Data_Pre/Emergencies_Data_Pre/'
    run(Emergencies_Data_Path)
