import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import numpy as np
import pandas as pd
import configparser
from Conf.loadconf import *
import DB.db_connects as dbconn

df_test = pd.DataFrame()
df_train = pd.DataFrame()

if DATA_FROM == 'MongoDB':
    client = dbconn.microrulemongoclient
    db = client['rule']
    test_collection = db['test_model_data']
    train_collection = db['train_model_data']

    test_cursor = test_collection.find({})
    train_cursor = train_collection.find({})

    df_test = pd.DataFrame(list(test_cursor))
    df_train = pd.DataFrame(list(train_cursor))

    df_test = df_test.replace('NA', np.NaN)
    df_train = df_train.replace('NA', np.NaN)
elif DATA_FROM == 'CSV':
    df_test = pd.read_csv(os.path.join(CSV_DATA_PATH, CSV_FILE_TEST))
    df_train = pd.read_csv(os.path.join(CSV_DATA_PATH, CSV_FILE_TRAIN))

h5filename = os.path.join(CSV_DATA_PATH, H5FILENAME)
store = pd.HDFStore(h5filename)
store['test'] = df_test
store['train'] = df_train

# store.put('test', df_test, format='table')
# store.put('train', df_train, format='train')
# df_test.to_hdf(h5filename,'test',mode='w', table=True )
# df_train.to_hdf(h5filename,'train',mode = 'w', table = True)
