import sys
import pandas as pd
sys.path.append("/home/python/credit")
import DB.db_connects as dbconn

client = dbconn.microrulemongoclient
db = client['rule']
test_collection = db['test_model_data']
train_collection = db['train_model_data']

test_cursor = test_collection.find({})
train_cursor = train_collection.find({})

df_test = pd.DataFrame(list(test_cursor))
df_train = pd.DataFrame(list(train_cursor))

store = pd.HDFStore('/home/python/data/dur/store.h5')
store['test'] = df_test
store['train'] = df_train
