import sys
import os
import numpy as np
import pandas as pd
sys.path.append("/home/python/credit")
import DB.db_connects as dbconn

CSV_DATA_PATH = '/home/python/data'
DATA_FROM = 'MongoDB'   # CSV

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
else if DATA_FROM == 'CSV':
    df_test = pd.read_csv(os.path.join(CSV_DATA_PATH, 'cs-test.csv' ))
    df_train = pd.read_csv(os.path.join(CSV_DATA_PATH, 'cs-training.csv' ))

h5filename = '/home/python/data/dur/store.h5'
store = pd.HDFStore(h5filename)
store['test'] = df_test
store['train'] = df_train

# store.put('test', df_test, format='table')
# store.put('train', df_train, format='train')
# df_test.to_hdf(h5filename,'test',mode='w', table=True )
# df_train.to_hdf(h5filename,'train',mode = 'w', table = True)
