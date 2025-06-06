'''
Давайте отберем заведения, где значение валюты, в которой принимают оплату, не пропущено.
Нужно сохранить данные в результирующий датафрейм result.
Данные загружены data.
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('/Users/anastasiamodenova/Downloads/data.csv')
result = data[~data['menus.currency'].isna()]
print(result)