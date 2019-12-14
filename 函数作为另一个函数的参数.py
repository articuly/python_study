# coding:utf-8
def opt(func, iterable):
    r = {func(i) for i in iterable}
    return r


st = opt(abs, (-1, 2, -3))
print(st)
