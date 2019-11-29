# coding:utf-8
def get_index(x, i, default=None):
    if -len(x) <= i < len(x):
        return x[i]
    else:
        return default


x = list(range(-10, 10))
print(get_index(x, 5))
print(get_index(x, -11))
print(get_index(x, 99))
print(get_index(x, 21, 'abc'))
