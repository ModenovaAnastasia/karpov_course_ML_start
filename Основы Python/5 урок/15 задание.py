'''
В этом задании нужно добавить столбец update_deltaс количеством целых дней, полученных от разницы между dateUpdated и dateAdded.
Потом для каждого города найдите (в указанном порядке):
- среднее по переменной update_delta
- широту самой северной закусочной (чем севернее расположена закусочная, тем больше будет значение широты)
Названия городов не должны быть индексами. Сохраните результирующий датафрейм в переменную result.
Также сохраните в переменную zep_mean среднее значение update_delta по городу Zephyrhills.
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('/Users/anastasiamodenova/Downloads/data.csv')
data['dateAdded'] = pd.to_datetime(data['dateAdded'])
data['dateUpdated'] = pd.to_datetime(data['dateUpdated'])
data['update_delta'] = (data['dateUpdated'] - data['dateAdded']).dt.days
result = data.groupby('city', as_index=False).agg({
    'update_delta': 'mean',
    'latitude': 'max'
})
zep_mean = result.loc[result['city'] == 'Zephyrhills', 'update_delta'].values[0]
print(result)
print(zep_mean)
