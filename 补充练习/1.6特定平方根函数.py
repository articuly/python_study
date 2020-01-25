# coding:utf-8
def func(*d):
    c, h = 50, 30
    lst = []
    for i in d:
        q = (2 * c * i / h) ** 0.5
        lst.append(int(q))
    return lst


print(func(100, 150, 180))
