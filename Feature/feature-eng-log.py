import sys
import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
sys.path.append("..")
import DB.db_connects as dbconn

client = dbconn.microrulemongoclient
db = client['rule']
test_collection = db['test_model_data']
train_collection = db['train_model_data']

test_cursor = test_collection.find({})
train_cursor = train_collection.find({})

df_test = pd.DataFrame(list(test_cursor))
df_train = pd.DataFrame(list(train_cursor))


#data = pd.read_csv('../data/cs-training.csv')
#test = pd.read_csv()

#"feature-eng description"
#data.describe().to_csv("desc-training.csv")

#a = np.log(data.RevolvingUtilizationOfUnsecuredLines+1)
