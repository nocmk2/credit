import sys
import numpy as np
import pandas as pd

store = pd.HDFStore('/home/python/data/dur/store.h5')
test = store['test']
train = store['train']

varneedtranslist = ['RevolvingUtilizationOfUnsecuredLines',
                    'NumberOfTime30-59DaysPastDueNotWorse',
                    'DebtRatio','MonthlyIncome','NumberOfOpenCreditLinesAndLoans',
                    'NumberOfTimes90DaysLate','NumberRealEstateLoansOrLines',
                    'NumberOfTime60-89DaysPastDueNotWorse','NumberOfDependents']

for v in varneedtranslist:
    with np.errstate(invalid='ignore'):
        test[v] = np.log(pd.to_numeric(test[v], errors='coerce') + 1)
        train[v] = np.log(pd.to_numeric(train[v], errors='coerce') + 1)

test.to_csv('~/data/testing-log-f10.csv')
train.to_csv('~/data/training-log-f10.csv')

store['test_log'] = test
store['train_log'] = train

# a = np.log(data.RevolvingUtilizationOfUnsecuredLines+1)

