'''
Отберите рестораны, у которых в колонке categories упоминается Pizza
Укажите индекс 3-го элемента, полученного после фильтрации
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('/Users/anastasiamodenova/Downloads/data.csv')
data1 = data[data['categories'].str.contains('Pizza', na=False)]
ind = data1.index[2]
print(ind)