'''
Перечислите первые три значения колонки dateAdded через запятую и пробел в том порядке, в котором они были выведены.
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('data.csv')
print(df.head(3))