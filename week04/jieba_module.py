import jieba
strings = ['我来自极客大学', 'Python进阶训练营真好玩']

for string in strings:
    result = jieba.cut(string, cut_all=False) # 精确模式
    print('Default Mode: ' + '/'.join(list(result)))

for string in strings:
    result = jieba.cut(string, cut_all=True) # 全模式
    print('Full Mode: ' + '/'.join(list(result)))

result = jieba.cut('钟南山院士接受采访新冠不会二次暴发')  # 默认是精确模式
print('/'.join(list(result)))

result = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造') # 搜索引擎模式
print('Search Mode: ' + '/'.join(list(result)))