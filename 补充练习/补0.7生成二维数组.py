# coding:utf-8
def foo(x, y):
    test = [[m * n for n in range(y)] for m in range(x)]
    return test


print(foo(3, 5))
