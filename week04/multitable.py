import pandas as pd
import numpy as np

group = ['x','y','z']
data1 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10)
    })

data2 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    })

data3 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10),
    "salary":np.random.randint(5,50,10),
    })

print(data1)
print(data2)
print(data3)

# print(pd.merge(data1, data2))

print(pd.merge(data3, data2, on='group'))

print('————————————————————————————')

print(pd.merge(data3, data2))

print('————————————————————————————')

print(pd.merge(data3, data2, left_on='age', right_on='salary'))

print('————————————————————————————')

print(pd.merge(data3, data2, on='group', how='inner'))

print('————————————————————————————')

print(pd.concat([data1, data2]))