
from snownlp import SnowNLP

text = '其实故事本来真的只值三星当初的中篇就足够了但是啊看到最后我又一次被东野叔的反战思想打动了所以就加多一星吧'
s = SnowNLP(text)

# print(s.words)
#
# print(list(s.tags))
#
# print(s.sentiments)

# text2 = '这本书烂透了'
# s2 = SnowNLP(text2)
# print(s2.sentiments)
#
# print(s2.pinyin)

# text3 = '後面這些是繁體字'
# s3 = SnowNLP(text3)
# print(s3.han)

print(s.keywords(limit=5))