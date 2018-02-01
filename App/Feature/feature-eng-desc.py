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


store = pd.HDFStore(os.path.join(CSV_DATA_PATH, H5FILENAME))
test = store['test']
train = store['train']

test_desc = test.describe()
train_desc = train.describe()

test_desc.to_csv(os.path.join(CSV_DATA_PATH,'desc-test.csv'))
train_desc.to_csv(os.path.join(CSV_DATA_PATH,'desc-training.csv'))

# save to h5
store['test_desc'] = test_desc
store['train_desc'] = train_desc

# save to mongo


# a = np.log(data.RevolvingUtilizationOfUnsecuredLines+1)

