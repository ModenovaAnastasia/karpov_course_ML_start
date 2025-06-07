'''
Сделайте группировку по месяцу открытия ресторана (переменная dateAdded). Сколько ресторанов было открыто в каждом месяце?
Рассчитайте по количеству уникальных id ресторанов в каждом месяце.
Значения dateAdded должны при этом быть индексами. Результирующий датафрейм сохраните в result
Данные сохранены в переменную data
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('data.csv')
data_1 = data.copy()
data_1['dateAdded'] = pd.to_datetime(data_1['dateAdded'])
data_1['month'] = data_1['dateAdded'].dt.month
result = data_1.groupby('month')['id'].nunique().to_frame()
print(result)