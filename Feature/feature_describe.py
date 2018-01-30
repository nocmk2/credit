import sys
import time
import pandas as pd
import numpy as np
from pymongo import MongoClient
import DB.db_connects as dbconn

fileid = sys.argv[1]

client = dbconn.microrulemongoclient
db = client['rule']

c_run_status = db['python_run_status']
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
run_status = {'_id':fileid,'type':'PythonDescribe','step':[{'step':'begin','time':nowtime},{'step':'train_end','time':''},{'step':'test_end','time':''},{'step':'end','time':''}]}
c_run_status.delete_one({"_id":fileid})
c_run_status.insert_one(run_status)

train_collection = db['train_model_data']
train_cursor = train_collection.find({"fileid":fileid})
df_train = pd.DataFrame(list(train_cursor))
df_train = df_train.replace('NA', np.NaN)
train_des_list = {}
train_des = df_train.describe()
for col in train_des.columns:
    traincoldata = train_des[col]
    dbtraincoldata = {}
    for colname in train_des.index:
        dbtraincoldata[colname] = str(traincoldata[colname])
    train_des_list[col] = dbtraincoldata
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
user_train_des = {"_id":fileid,"inputtime":nowtime,"desdata":train_des_list}
c_train_model_des = db['train_model_des']
c_train_model_des.delete_one({"_id":fileid})
c_train_model_des.insert_one(user_train_des)

nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
run_status['step'][1] = {'step':'train_end','time':nowtime}
c_run_status.delete_one({"_id":fileid})
c_run_status.insert_one(run_status)

test_collection = db['test_model_data']
test_cursor = test_collection.find({"fileid":fileid})
df_test = pd.DataFrame(list(test_cursor))
df_test = df_test.replace('NA', np.NaN)
test_des_list = {}
test_des = df_test.describe()
for col in test_des.columns:
    testcoldata = test_des[col]
    dbtestcoldata = {}
    for colname in test_des.index:
        dbtestcoldata[colname] = str(testcoldata[colname])
    test_des_list[col] = dbtestcoldata
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
user_test_des = {"_id":fileid,"inputtime":nowtime,"desdata":test_des_list}
c_test_model_des = db['test_model_des']
c_test_model_des.delete_one({"_id":fileid})
c_test_model_des.insert_one(user_test_des)

nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
run_status['step'][2] = {'step':'test_end','time':nowtime}
run_status['step'][3] = {'step':'end','time':nowtime}
c_run_status.delete_one({"_id":fileid})
c_run_status.insert_one(run_status)

