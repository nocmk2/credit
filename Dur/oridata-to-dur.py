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

h5filename = '/home/python/data/dur/store.h5'
store = pd.HDFStore(h5filename)
store.put('test', df_test, format='table')
store.put('train', df_train, format='train')
# df_test.to_hdf(h5filename,'test',mode='w', table=True )
# df_train.to_hdf(h5filename,'train',mode = 'w', table = True)
