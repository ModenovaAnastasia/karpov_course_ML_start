'''
Давайте найдем рестораны, открытые в октябре.
В качестве ответа отправьте индексы первых пяти записей, соответствующих ресторанам, открытым в октябре (ресторан может повторяться).
Ответ запишите через запятую и пробел в порядке возрастания.
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
data = pd.read_csv('data.csv')
data_1 = data.copy()
data_1['dateAdded'] = pd.to_datetime(data_1['dateAdded'])
october_data = data_1[data_1['dateAdded'].dt.month == 10]
print(', '.join(map(str, october_data.index[:5])))