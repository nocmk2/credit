import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import numpy as np
import pandas as pd
from Conf.loadconf import *

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

