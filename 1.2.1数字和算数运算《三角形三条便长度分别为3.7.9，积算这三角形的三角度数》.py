# coding:utf-8
# c^2 = a^2 + b^2 - 2ab*cosC
import math

a, b, c = 3, 7, 9
A = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
B = math.acos((c ** 2 + a ** 2 - b ** 2) / (2 * c * a))
C = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
print("A角的弧度是：", A)
print("B角的弧度是：", B)
print("C角的弧度是：", C)
print("A角的角度是：", A * 180 / math.pi)
print("B角的角度是：", B * 180 / math.pi)
print("C角的角度是：", C * 180 / math.pi)
