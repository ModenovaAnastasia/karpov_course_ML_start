'''
Отберите заведения, которые находятся в городе Калифорния ('California'), штат Миссури.
Укажите индексы, под которыми полученные заведения расположены в датафрейме, через запятую и пробел в порядке возрастания.
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('data.csv')
f_df=df[(df['city'] == 'California')]
print(f_df.index)