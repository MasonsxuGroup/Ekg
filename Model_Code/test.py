import pandas as pd
from LAC import LAC
from tqdm.std import trange


def marker_data(all_data):
    extract_data_lists = []
    print('转换标记，并拆分字符串：')
    for item_index in trange(len(all_data)):
        item = all_data[item_index]
        if item[1] == 'O':
            extract_data_list = []
            extract_data_list.append(item[0])
            extract_data_list.append(item[1])
            number_data = ''
            if len(extract_data_list) == 2:
                extract_data_lists.append(extract_data_list)
        else:
            marker_len = len(extract_data_lists)
            number_data = ''
            for index in range(0, len(item[0])):  # 拆分字符串，并合并字符串中的数字
                extract_data_list = []
                # 判断是否为字符串的开始 index，并设置长度避免超出字符串 index
                if (str(item[0][index]).isdigit() is False) or (index == len(item[0]) - 1):
                    marker = 'I-' + item[1]
                    extract_data_list.append(item[0][index])
                    extract_data_list.append(marker)
                elif (str(item[0][index]).isdigit()) and (str(item[0][index + 1]).isdigit()):
                    number_data += str(item[0][index])
                elif str(item[0][index]).isdigit() and (str(item[0][index + 1]).isdigit() is False):
                    number_data += str(item[0][index])
                    marker = 'I-' + item[1]
                    extract_data_list.append(number_data)
                    extract_data_list.append(marker)
                    number_data = ''
                if len(extract_data_list) == 2:
                    extract_data_lists.append(extract_data_list)
            extract_data_lists[marker_len][1] = 'B' + \
                extract_data_lists[marker_len][1][1:]
    extract_data_lists.append('')
    return extract_data_lists


# 使用自己训练好的模型
my_lac = LAC(model_path='Model_Code/model/')
my_lac.load_customization('Model_Code/data/dict.txt', sep=None)

data = pd.read_csv('Model_Code/data/G_all_marked_data.txt', header=None)
data = data.values.tolist()
texts = []
for data_index in trange(len(data)):
    line = data[data_index][0]
    texts.append(line)
lac_result = my_lac.run(texts[:10])

sheet = pd.DataFrame(lac_result)
sheet.to_csv('Model_Code/result/result_lac.csv', index=None, header=None)

items_list = []
for data_index in trange(len(lac_result)):
    word_list = lac_result[data_index][0]
    tag_list = lac_result[data_index][1]
    for word_index in range(0, len(word_list)):
        item_list = []
        item_list.append(word_list[word_index])
        item_list.append(tag_list[word_index])
        items_list.append(item_list)

# extract_data_lists = marker_data(items_list)
# print(extract_data_lists)
sheet = pd.DataFrame(items_list)
sheet.to_csv('Model_Code/result/result.csv', index=None, header=None)
