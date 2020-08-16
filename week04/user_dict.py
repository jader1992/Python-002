import jieba
string = '极客大学Python进阶训练营真好玩'
user_dict=r'extra_dict/user_dict.txt'

# 自定义词典
jieba.load_userdict(user_dict)

result = jieba.cut(string, cut_all=False)
print('自定义: ' + '/'.join(list(result)))

print('='*40)

jieba.add_word('极客大学')

result = jieba.cut(string, cut_all=False)
print('动态添加: ' + '/'.join(list(result)))