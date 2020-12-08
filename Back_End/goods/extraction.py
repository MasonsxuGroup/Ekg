import json
import pandas as pd
from LAC import LAC


class ExtractData:
    def load_customization(text):
        """加载训练好的模型

        Args:
            :text (str): customization of the text，待提取的文本字符串

        Returns:
            :result_data_dict (dict): dictionary with customization of the text，提取后的文本字典
        """

        my_lac = LAC(model_path='Model_Code/model/')
        my_lac.load_customization('Model_Code/data/dict.txt', sep=None)
        result_list = my_lac.run(text)
        result_data_dict = {}
        result_data_dict["data"] = []
        for index in range(len(result_list[0])):
            result_dict = {}
            result_dict["item"] = result_list[0][index]
            result_dict["pos"] = result_list[1][index]
            result_data_dict["data"].append(result_dict)
        file_path = 'Back_End/static/data/result_data_dict.json'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(result_data_dict).replace("'", '"'))
        return result_data_dict

    def load_figure_data():
        """加载提取后的文本字典

        Args:
            :result_data_dict (dict): dictionary with customization of the text，提取后的文本字典

        Returns:
            :result_data_dict (dict): dictionary with customization of the text，提取后的文本字典
        """

        file_path = 'Back_End/static/data/result_data_dict.json'
        result_data_dict = pd.read_json(file_path, encoding='utf-8')
        figure_data_dict = {}
        figure_data_dict['data'] = []
        result_dict = {}
        result_dict["LOC"] = []
        result_dict["TIME"] = []
        result_dict["RES"] = []
        for index, row in enumerate(result_data_dict['data']):
            if row["pos"] == 'LOC':
                if len(result_dict["LOC"]) != 0:
                    figure_data_dict['data'].append(result_dict)
                    result_dict = {}
                    result_dict["LOC"] = []
                    result_dict["TIME"] = []
                    result_dict["RES"] = []
                result_dict["LOC"] = row["item"]
            elif row["pos"] == 'TIME' and row["item"] not in result_dict["TIME"]:
                result_dict["TIME"].append(row["item"])
            elif row["pos"] == 'RES' and row["item"] not in result_dict["RES"]:
                result_dict["RES"].append(row["item"])
            if index == (len(result_data_dict['data'])-1):
                figure_data_dict['data'].append(result_dict)
        return figure_data_dict
