import jieba.analyse

text = '机器学习，需要一定的数学基础，需要掌握的数学基础知识特别多，如果从头到尾开始学，估计大部分人来不及，我建议先学习最基础的数学知识'
# 基于TF-IDF算法进行关键词抽取

# tfidf = jieba.analyse.extract_tags(text,
#         topK= 5,
#         withWeight=True
#         )

textrank = jieba.analyse.textrank(text,
topK= 5,
        withWeight=True
                                  )

print(textrank)