from LAC import LAC


class ExtractData:
    def load_customization(text):
        # 加载训练好的模型
        my_lac = LAC(model_path='Model_Code/model/')
        my_lac.load_customization('Model_Code/data/dict.txt', sep=None)
        result_list = my_lac.run(text)
        result_data_dict = {}
        result_data_dict['data'] = []
        for index in range(len(result_list[0])):
            result_dict = {}
            result_dict[result_list[0][index]] = result_list[1][index]
            result_data_dict['data'].append(result_dict)
        return result_data_dict
