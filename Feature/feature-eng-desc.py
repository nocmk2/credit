import sys
import numpy as np
import pandas as pd
import pickle
sys.path.append("/home/python/credit")
import DB.db_connects as dbconn

store = pd.HDFStore('/home/python/data/dur/store.h5')
test = store['test']
train = store['train']

test.describe().to_csv("~/data/desc-training.csv")
train.describe().to_csv("~/data/desc-testing.csv")

# a = np.log(data.RevolvingUtilizationOfUnsecuredLines+1)

