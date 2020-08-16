import pandas as pd
import numpy as np

group = ['x','y','z']
data1 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10)
    })

# print(data1)
#
# data1.to_excel( excel_writer = r'file.xlsx')

data1.to_excel(excel_writer=r'file.xlsx', sheet_name='sheet2', index=False, columns = ['group','age'])
