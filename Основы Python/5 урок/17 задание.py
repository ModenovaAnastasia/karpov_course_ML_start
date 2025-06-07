'''
В этом задании снова нужно добавить столбец update_delta, куда будет записана разница в днях между dateUpdated и dateAdded.
Посчитайте среднее и медиану получившейся колонки.
Перечислите значения через пробел (сначала среднее, затем медиану), округлив до 2 знаков.
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('data.csv')

data['dateAdded'] = pd.to_datetime(data['dateAdded'])
data['dateUpdated'] = pd.to_datetime(data['dateUpdated'])
data['update_delta'] = (data['dateUpdated'] - data['dateAdded']).dt.days
mean_delta = data['update_delta'].mean()
median_delta = data['update_delta'].median()
print(mean_delta, median_delta)