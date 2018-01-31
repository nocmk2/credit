import sys
import numpy as np
import pandas as pd
import pickle
sys.path.append("/home/python/credit")
import DB.db_connects as dbconn

store = pd.HDFStore('/home/python/data/dur/store.h5')
test = store['test']
train = store['train']

test_desc = test.describe()
train_desc = train.describe()

test_desc.to_csv("~/data/desc-training.csv")
train_desc.to_csv("~/data/desc-testing.csv")

store['test_desc'] = test_desc
store['train_desc'] = train_desc

# a = np.log(data.RevolvingUtilizationOfUnsecuredLines+1)

