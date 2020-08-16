import pandas as pd
import numpy as np

# 聚合
sales = [{'account': 'Jones LLC','type':'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co','type':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc','type':'a',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]

df2 = pd.DataFrame(sales)

# for a,b in df2.groupby('type'):
#     print(a)
#     print('-------')
#     print(b)
#     print('-------')

# print(df2.groupby('type').count())
# print(df2.groupby('type').sum())

# print(df2.groupby('type').aggregate({'type':'count', 'Feb':'sum'}))

group=['x','y','z']

data=pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    "age":np.random.randint(15,50,10)
    })

print(data)

# print(data.groupby('group').agg('mean'))
# print(data.groupby('group').mean().to_dict())
# print(data.groupby('group').transform('mean'))

print(pd.pivot_table(data, values='salary', columns='group', index='age', aggfunc='count',margins=True).reset_index())