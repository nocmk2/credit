import sys
import numpy as np
import pandas as pd
import pickle
sys.path.append("/home/python/credit")
import DB.db_connects as dbconn

dur_file_test = open("~/data/dur/test.pickle")
dur_file_train = open("~/data/dur/train.pickle")

test = pickle.load(dur_file_test)
train = pickle.load(dur_file_train)

df_test = pd.DataFrame(list(test))
df_train = pd.DataFrame(list(train))

df_train.describe().to_csv("~/data/desc-training.csv")
df_test.describe().to_csv("~/data/desc-testing.csv")

# a = np.log(data.RevolvingUtilizationOfUnsecuredLines+1)

