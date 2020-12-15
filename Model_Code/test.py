import random
import pandas as pd
from LAC import LAC
from tqdm.std import trange


# 使用自己训练好的模型
my_lac = LAC(model_path='Model_Code/model/')
my_lac.load_customization('Model_Code/data/dict.txt', sep=None)

data = pd.read_csv('Model_Code/data/G_all_marked_data.txt', header=None)
data = data.values.tolist()
texts = []
for data_index in trange(len(data)):
    line = data[data_index][0]
    texts.append(line)
start = random.randint(0, len(data) - 10)
lac_result = my_lac.run(texts[start : start + 10])

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

sheet = pd.DataFrame(items_list)
sheet.to_csv('Model_Code/result/result.csv', index=None, header=None)
