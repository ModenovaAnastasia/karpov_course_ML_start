'''
Напишите через запятую и пробел 5 городов с наибольшим количеством записей
(в порядке убывания количества записей).
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('/Users/anastasiamodenova/Downloads/data.csv')
top_cities = data['city'].value_counts().head(5)
print(top_cities)