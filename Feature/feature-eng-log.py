import sys
import numpy as np
import pandas as pd
import pickle
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

df_train.describe().to_csv("~/data/desc-training.csv")
df_test.describe().to_csv("~/data/desc-testing.csv")

file_test = open("~/data/dur/test.pickle","w")
file_train = open("~/data/dur/train.pickle","w")

pickle.dump(df_test, file_test, 0)
pickle.dump(df_train, file_train, 0)

file_test.close()
file_train.close()

# a = np.log(data.RevolvingUtilizationOfUnsecuredLines+1)

