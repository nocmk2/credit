import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
import numpy as np
import pandas as pd
from Conf.loadconf import *
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import DB.db_connects as dbconn
import DB.db_mongoimg as mongoImg
#import gridfs

store = pd.HDFStore(os.path.join(CSV_DATA_PATH, H5FILENAME))
test = store['test']
train = store['train']

PNG_PATH = os.path.join(CSV_DATA_PATH,'png')

scatter_matrix(train, alpha=0.2,figsize=(26, 26), diagonal='kde')
plt.savefig(os.path.join(PNG_PATH,'train_scatter_matrix.png'))

'''
figfile = open(os.path.join(CSV_DATA_PATH,'train_scatter_matrix.png'),'rb')
# save to mongoDB
client = dbconn.microrulemongoclient
db = client['rule']
fsb = gridfs.GridFSBucket(db)
a = fsb.upload_from_stream("pp", figfile)
# http://api.mongodb.com/python/current/api/gridfs/
# f = fs.find_one({"filename": "train_scatter_matrix.png"})
file = open(os.path.join(CSV_DATA_PATH,'11train_scatter_matrix.png'), 'w')

fsb.download_to_stream_by_name("pp",file)

file.close()
# print(fs.get("5a7ae64eadf09013639c6000").read())
'''
client = dbconn.microrulemongoclient
db = client.rule
m = mongoImg.mongoImg(db,PNG_PATH)
m.deleteAll()
m.insert()
print(m.list())
m.getbyname('train_scatter_matrix.png','/Users/zhangmk/Downloads/data/backup.png')


