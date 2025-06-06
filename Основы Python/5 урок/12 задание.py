'''
Посчитайте, сколько ресторанов Taco Bell находится в каждом городе. Отберите 5 городов, в которых ресторан встречается чаще всего.
Количество ресторанов для этих городов с их названиями сохраните в виде объекта pd.Series в переменную result.
Данные сохранены в переменную data
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('/Users/anastasiamodenova/Downloads/data.csv')
df=data[data['name'] == 'Taco Bell']
result = df['city'].value_counts().head(5)
print(result)