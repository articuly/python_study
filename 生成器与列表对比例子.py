# coding:utf-8
def gensquares(N):
    for i in range(N):
        yield i ** 2


for item in gensquares(5):
    print(item)


def gensquares1(N):
    res = []
    for i in range(N):
        res.append(i*i)
    return res


for item in gensquares1(5):
    print(item)
