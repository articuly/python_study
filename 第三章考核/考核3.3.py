# coding:utf-8
# 计算三维坐标系统中两点的直线距离
import math


def distance_in_space(a: tuple, b: tuple):
    try:
        d = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
        return d
    except TypeError:
        print('请输入包含三个数字的元组作为参数')


x = (5, 6, 7)
y = (8, 9, 9)
print(distance_in_space(x, y))
# z = ('l', 's', 'd')
# print(distance_in_space(x, z))


# 简化的方法
x = (5, 6, 7)
y = (8, 9, 9)
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
