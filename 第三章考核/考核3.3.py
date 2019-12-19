# coding:utf-8
import math


def distance_in_space(a: tuple, b: tuple):
    try:
        d = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
        return d
    except TypeError:
        print('请输入数字')


x = (5, 6, 7)
y = (8, 9, 9)
print(distance_in_space(x, y))
