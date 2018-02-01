import sys
import os
import configparser
config = configparser.ConfigParser()
config.readfp(open(os.path.join(os.path.dirname(__file__), 'main.conf')))
CSV_DATA_PATH = config.get('data_source', 'csv_data_path')
DATA_FROM = config.get('data_source', 'ori_data_from')
CSV_FILE_TEST = config.get('data_source', 'csv_file_test')
CSV_FILE_TRAIN = config.get('data_source', 'csv_file_train')
H5FILENAME = config.get('data_source', 'h5filename')
WORK_PATH = config.get('data_source', 'work_path')

