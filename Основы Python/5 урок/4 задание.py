'''
Какие средние значения в тех колонках, которые вывел describe в предыдущем задании?
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('data.csv')
desc = df.describe()
means = desc.loc['mean']
print(means)