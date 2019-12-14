# coding:utf-8
def dct(n):
    d = {i: i * i for i in range(1, n + 1)}
    print(d)
    return dct


dct(8)
