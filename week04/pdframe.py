
import pandas as pd
import numpy as np

df1 = pd.DataFrame(['a', 'b', 'c', 'd'])

df2 = pd.DataFrame([['a','b'], ['c', 'd']])
print(df2)

df2.columns= ['one', 'two']
df2.index = ['first', 'second']

print(df2)

df3 = pd.DataFrame([['a','b'], ['c', 'd']], columns=['one', 'two'], index=['first', 'second'])
print(df3)