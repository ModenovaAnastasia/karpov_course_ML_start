'''
В этом задании нужно отобрать записи, у которых более 20 категорий, далее их нужно сгруппировать по провинциям
и подсчитать минимальную longitude в каждой. Округлите значения longitude до 3-х знаков после запятой.
Далее сохраните результирующий датафрейм в файл в формате csv с сепаратором ;.
Сам датафрейм должен содержать две колонки: province и longitude
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('data.csv')

data['categories_count'] = data['categories'].str.count(',') + 1
filtered = data[data['categories_count'] > 20]
result = filtered.groupby('province')['longitude'].min().reset_index()
result['longitude'] = result['longitude'].round(3)
result.to_csv('result.csv', sep=';', index = False)
print(result)