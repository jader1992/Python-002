
import numpy as np
import pandas as pd
import matplotlib as plt
import os

pwd = os.path.dirname(__file__) #获取当前执行文件的绝对路径
book = os.path.join(pwd, 'book_utf8.csv')
df = pd.read_csv(book)  #读取文件
# df = pd.read_csv('book_utf8.csv')
# print(df)

# print(df['还行'])
df.columns = ['star', 'vote', 'shorts']
# print(df)

loc = df.loc[1:3, ['star']]
# print(loc)

check = df['star'] == '力荐'
# print(df[check])

df = df.dropna()

starSum = df.groupby('star').sum()
# print(starSum)


star_to_number = {
    "力荐": 5,
    "很差": 4,
    "推荐": 3,
    "较差": 2,
    "还行": 1
}

df['new_star'] = df['star'].map(star_to_number)
# print(df)

check = df['new_star'] >=3
print(df[df['new_star'] >= 3])

