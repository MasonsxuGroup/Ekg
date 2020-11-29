from LAC import LAC

# 选择使用默认的词法分析模型
lac = LAC()

# 训练和测试数据集，格式一致
train_file = "Model_Code/data/train.tsv"
test_file = "Model_Code/data/test.tsv"
lac.train(model_save_dir='Model_Code/model/',
          train_data=train_file, test_data=test_file)
