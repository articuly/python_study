# coding:utf-8
def fact(n):
    s = 1
    for i in range(1, n + 1):
        s = s * i
    return s


print(fact(8), fact(9), fact(7), fact(10), fact(6), sep=', ')
