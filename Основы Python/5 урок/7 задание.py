'''
Отберите заведения Taco Bell в городе Калифорния ('California'), штат Миссури.
Укажите индексы этих заведений через запятую и пробел в порядке возрастания
'''

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('/Users/anastasiamodenova/Downloads/data.csv')
f_df=df[(df['city'] == 'California') & (df['name'] == 'Taco Bell')]
print(f_df.index)