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

        try:
            my_lac = LAC(model_path='Model_Code/model/')
            my_lac.load_customization('Model_Code/data/dict.txt', sep=None)
            result_list = my_lac.run(text)
            result_data_dict = {}
            result_data_dict["data"] = []
            number_data = ''
            for index in range(len(result_list[0])):
                result_dict = {}
                if ((str(result_list[0][index]).isdigit() is False) and (str(result_list[0][index][:-1]).isdigit() is False)) or ((index == len(result_list[0]) - 1) and (number_data == '')):
                    result_dict["item"] = result_list[0][index]
                    result_dict["pos"] = result_list[1][index]
                    result_data_dict["data"].append(result_dict)
                elif (index == len(result_list[0]) - 1) and (number_data != ''):
                    number_data += result_list[0][index]
                    result_dict["item"] = number_data
                    result_dict["pos"] = result_list[1][index]
                    result_data_dict["data"].append(result_dict)
                elif (str(result_list[0][index]).isdigit()) and ((str(result_list[0][index+1]).isdigit()) or (str(result_list[0][index+1][:-1]).isdigit())):
                    number_data += result_list[0][index]
                elif ((str(result_list[0][index][:-1]).isdigit()) or (str(result_list[0][index]).isdigit())) and (str(result_list[0][index+1]).isdigit() is False):
                    number_data += result_list[0][index]
                    result_dict["item"] = number_data
                    result_dict["pos"] = result_list[1][index]
                    result_data_dict["data"].append(result_dict)
                    number_data = ''
            file_path = 'static/data/result_data_dict.json'
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(result_data_dict).replace("'", '"'))
            return result_data_dict
        except Exception as e:
            print(e)
            return {}

    def load_figure_data():
        """加载提取后的文本字典

        Args:
            :result_data_dict (dict): dictionary with customization of the text，提取后的文本字典

        Returns:
            :result_data_dict (dict): dictionary with customization of the text，提取后的文本字典
        """

        try:
            file_path = 'static/data/result_data_dict.json'
            result_data_dict = pd.read_json(file_path, encoding='utf-8')
            figure_data_dict = {}
            figure_data_dict['data'] = []
            result_dict = {}
            result_dict["LOC"] = []
            result_dict["TIME"] = []
            result_dict["RES"] = []
            result_dict["ORG"] = []
            result_dict["PER"] = []
            for index, row in enumerate(result_data_dict['data']):
                if row["pos"] == 'LOC':
                    if len(result_dict["LOC"]) != 0:
                        figure_data_dict['data'].append(result_dict)
                        result_dict = {}
                        result_dict["LOC"] = []
                        result_dict["TIME"] = []
                        result_dict["RES"] = []
                        result_dict["ORG"] = []
                        result_dict["PER"] = []
                    result_dict["LOC"] = row["item"]
                elif row["pos"] == 'TIME' and row["item"] not in result_dict["TIME"]:
                    result_dict["TIME"].append(row["item"])
                elif row["pos"] == 'RES' and row["item"] not in result_dict["RES"]:
                    result_dict["RES"].append(row["item"])
                elif row["pos"] == 'ORG' and row["item"] not in result_dict["ORG"]:
                    result_dict["ORG"].append(row["item"])
                elif row["pos"] == 'PER' and row["item"] not in result_dict["PER"]:
                    result_dict["PER"].append(row["item"])
                if index == (len(result_data_dict['data'])-1):
                    figure_data_dict['data'].append(result_dict)
            return figure_data_dict
        except Exception as e:
            print(e)
            return {}
