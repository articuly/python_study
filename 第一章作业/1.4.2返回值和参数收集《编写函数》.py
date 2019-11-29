# coding:utf-8
# 方法一
def Distance(x1, y1, x2, y2):
    import math
    if all([isinstance(i, (int, float)) for i in (x1, y1, x2, y2)]):
        # if all((isinstance(x1, (int, float)), isinstance(y1, (int, float)), isinstance(x2, (int, float)), isinstance(y2, (int, float)))):
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        print("直角坐标系中两点的距离是", d)
        return d
    else:
        print("请在函数中输入两点坐标的数值！")


# 方法二
def Dis(x1, y1, x2, y2):
    import math
    try:
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        print("直角坐标系中两点的距离是", d)
        return d
    except TypeError:
        print("请在函数中输入两点坐标的数值！")


Distance(1, 2.5, -3, -4.99)
Distance(1, 2.5, -3, "ll")
Dis(1, 2, -1, -2)
Dis(1, 2.5, -3, "ll")

st = {'a', 'b', 'c'}


def letter_set(s):
    if set(s) & st == set():
        print('字符串不包含指定集合中的字母。')
    else:
        print('字符串包含指定集合中的字母。')


letter_set('apple')
letter_set('foot')
letter_set('carbon')
