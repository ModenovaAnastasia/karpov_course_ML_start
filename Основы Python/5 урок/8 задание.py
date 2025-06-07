'''
Давайте найдем заведения Taco Bell или заведения, которые находятся в городе Нью-Йорк.
При этом обязательно, чтобы в названии меню не было Volcano Taco и Fresco Soft Taco (именно таких значений колонки).
Данные нужно сохранить в датафрейм result.
Данные загружены в переменную data.
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('data.csv')
result=data[
    (((data['name'] == 'Taco Bell') | (data['city'] == 'New York')) & (~(data['menus.name'].isin(['Volcano Taco', 'Fresco Soft Taco']))))
]
print(result)