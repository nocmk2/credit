import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import numpy as np
import pandas as pd
from Conf.loadconf import *
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

store = pd.HDFStore(os.path.join(CSV_DATA_PATH, H5FILENAME))
test = store['test']
train = store['train']

scatter_matrix(train, alpha=0.2,figsize=(26, 26), diagonal='kde')
plt.savefig(os.path.join(CSV_DATA_PATH,'train_scatter_matrix.png'))

# save to h5




