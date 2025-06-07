'''
Сейчас в данных присутствуют пропущенные значения. Давайте их удалим.
Примените метод dropna.  Сколько осталось записей?
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('/Users/anastasiamodenova/Downloads/data.csv')
data1 = data.dropna()
print(len(data1))