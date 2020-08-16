import pandas as pd
import numpy as np
import re

# print(pd.Series(['a','b','c']))

s1 = pd.Series({'a':"测试",'b':"hh",'c':33})

s2 = pd.Series([11,22,33], index=['a', 'b', 'c'])

# print(s1.index, s1.values)
# print(type(s1.values))

print(s1.values.tolist())

emails = pd.Series(['abc at amazom.com', 'admin1@163.com', 'mat@m.at', 'ab@abc.com'])
pattern = '[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z0-9]{2,5}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
print(mask)
print(emails[mask])