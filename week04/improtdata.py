import pandas as pd
import pymysql
# pip install xlrd
# 导入excel文件
execl1 = pd.read_excel(r'1.xlsx')
print(execl1)
# print(execl1.head(1))

print(pd.read_excel(r'1.xlsx',sheet_name=0).describe())


csv1 = pd.read_csv(r'book_utf8.csv', sep=',', nrows=10, encoding='utf-8')
print(csv1)

sql = 'select * from movie'
conn = pymysql.connect(
            host='127.0.0.1',
            port= 3306,
            user= 'root',
            password= '12345678',
            db= 'test',
            charset= 'utf8'
)
df = pd.read_sql(sql,conn)
print(df)