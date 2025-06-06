'''
Попробуйте сделать data['categories'], data[['categories']],
посмотрите на тип и на значения их элементов.
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('/Users/anastasiamodenova/Downloads/data.csv')
print(type(data['categories']))
print(data['categories'].head())
print(type(data[['categories']]))
print(data[['categories']].head())