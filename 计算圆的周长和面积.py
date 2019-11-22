# coding:utf-8
# 输入圆的半径来计算圆的周长和面积
# 可以加入isdigit的判断
r = input("请输入一个数字：")
import math

r = float(r)
c = 2 * math.pi * r
a = math.pi * r ** 2
print(round(c, 2))
print(round(a, 2))
