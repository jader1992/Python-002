
from sklearn import datasets

iris = datasets.load_iris()
x, y = iris.data, iris.target

# 查看特征
print(iris.feature_names)

# 查看标签
print(iris.target_names)

## 按照3比1的比例划分训练集和测试集

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

print(X_train, X_test, y_train, y_test)