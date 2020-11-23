from datetime import date
import os
import pandas as pd
from pandas.core.indexes.datetimes import date_range


def get_data(folderpath_origin):
    filename = os.listdir(folderpath_origin)
    all_data = []
    for name in filename:
        path = folderpath_origin + name
        if path[-5:] == '.xlsx':
            data = pd.read_excel(path)
            abstracts = data['摘要'].to_list()
            for abstract in abstracts:
                abstract = str(abstract).replace('\u200b', '').replace(
                    ' ', '').replace('\\', '').replace('#', '').replace('@', '').replace('/', '').replace('.', '')
                all_data.append(abstract)
        elif path[-4:] == '.csv':
            data = pd.read_csv(path)
            detaileds = data['详细'].to_list()
            for detailed in detaileds:
                detailed = str(detailed).replace('\u200b', '').replace(
                    ' ', '').replace('\\', '').replace('#', '').replace('@', '').replace('/', '').replace('.', '')
                all_data.append(detailed)
    return all_data


def pre_data(data):
    Pre_Data = []
    for row_data in data:
        new_row_data = ''
        date_data = ''
        for index in range(0, len(row_data)):
            if (str(row_data[index]).isdigit() is False) or (index == len(row_data) - 1):
                new_row_data = row_data[index] + ' O'
                Pre_Data.append(new_row_data)
            elif (str(row_data[index]).isdigit()) and (str(row_data[index + 1]).isdigit()):
                date_data += str(row_data[index])
            elif str(row_data[index]).isdigit() and (str(row_data[index + 1]).isdigit() is False):
                date_data += str(row_data[index])
                new_row_data = date_data + ' O'
                Pre_Data.append(new_row_data)
                date_data = ''
        Pre_Data.append(' ')
    return Pre_Data


def save_mean_data(data, amount, folderpath_dest):
    all_data_length = len(data)
    mean_data_length = all_data_length//amount
    start = 0
    end = mean_data_length
    for index in range(0, amount):
        while data[end - 1] != ' ':
            end += 1
        else:
            sheet = pd.DataFrame(data[start:end - 1])
            filename = folderpath_dest + 'Emergencies_Part_' + \
                str(index) + '.txt'
            sheet.to_csv(filename, index=None, header=None)
            start = end
            end += mean_data_length
            if end > all_data_length:
                end = all_data_length


def save_all_data(data, folderpath_dest):
    filename = folderpath_dest + 'Emergencies_All_Data.txt'
    sheet = pd.DataFrame(data)
    sheet.to_csv(filename, index=None, header=None)


def run(folderpath_origin, folderpath_dest, amount):
    all_data = get_data(folderpath_origin)
    print('加载数据完毕！！！')
    already_pre_data = pre_data(all_data)
    print('数据处理完毕！！！')
    save_all_data(already_pre_data, folderpath_dest)
    print('保存所有已处理数据！！！')
    save_mean_data(already_pre_data, amount, folderpath_dest)
    print('均分保存所有数据，并保存！！！')


if __name__ == "__main__":
    News_Data_Origin_Path = 'Data_Pre/News_Data_Origin/'
    Emergencies_Data_Path = 'Data_Pre/Emergencies_Data_Pre/'
    amount = 5
    run(News_Data_Origin_Path, Emergencies_Data_Path, amount)
