from LAC import LAC


def load_customization(text):
    # 加载训练好的模型
    my_lac = LAC(model_path='Model_Code/model/')
    my_lac.load_customization('Model_Code/data/dict.txt', sep=None)
    result_list = my_lac.run(text)
    result_dict = {}
    for index in range(len(result_list[0])):
        result_dict[result_list[0][index]] = result_list[1][index]
    return result_dict


# if __name__ == '__main__':
#     load_customization('美国连续4天新增确诊超5万例，当地专家警告再不采取正确的预防措施，情况只会更糟。')
