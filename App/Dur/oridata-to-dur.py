import sys
import os
import numpy as np
import pandas as pd
import configparser
config = configparser.ConfigParser()
config.readfp(open(sys.path[0] + '/../Conf/main.conf'))
CSV_DATA_PATH = config.get('data_source', 'csv_data_path')
DATA_FROM = config.get('data_source', 'ori_data_from')
CSV_FILE_TEST = config.get('data_source', 'csv_file_test')
CSV_FILE_TRAIN = config.get('data_source', 'csv_file_train')
H5FILENAME = config.get('data_source', 'h5filename')
WORK_PATH = config.get('data_source', 'work_path')
df_test = pd.DataFrame()
df_train = pd.DataFrame()

if DATA_FROM == 'MongoDB':
    sys.path.append(WORK_PATH)
    import DB.db_connects as dbconn
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
