
import pandas as pd

df=pd.DataFrame({"A":[5,3,None,4],
                 "B":[None,2,4,3],
                 "C":[4,3,8,5],
                 "D":[5,4,2,None]})

# print(df[['A', 'C']])
#
# print(df.iloc[:,[0,2]])
#
# print(df.iloc[[0,2],[0,2]])
#
# print(df.iloc[0:3])
#
# print(df[ (df['A'] < 5) & (df['C']<4) ] )

# print(df['C'].replace(4,40))
# print(df.replace([4,5,8],200))
# print(df.replace({4:400,5:500,8:800}))

# print(df.sort_values(by=['A'], ascending=False))
# print(df.sort_values(by=['A','C'], ascending=[True, False]))

# print(df.drop('A', axis=1))
# print(df.drop(3, axis=0))
# print(df[df['A'] < 4])

# print(df)
# print(df.T)
# print(df.T.T)

df4 = df4 = pd.DataFrame([
                     ['a', 'b', 'c'],
                     ['d', 'e', 'f']
                    ],
                    columns= ['one', 'two', 'three'],
                    index = ['first', 'second']
                   )
# print(df4)
print(df4.stack())
print(df4.unstack())
print(df4.stack().reset_index())