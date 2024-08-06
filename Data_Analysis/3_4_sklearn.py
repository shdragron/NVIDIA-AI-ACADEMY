# 3_4_sklearn.py

from sklearn import datasets

def sk_1():
    # load, make, fetch
    iris = datasets.load_iris()
    print(iris)
    print(iris.keys)
    print(iris['data']) # [5.9 3.  5.1 1.8] Sepal: length width, Petal: length width

    print(iris['target_names']) # label
    print(iris['feature_names'])
    print(iris['target']) # target_names의 index화 0은 'setosa'


sk_1()