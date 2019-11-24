# coding:utf-8
def Distance(x1, y1, x2, y2):
    import math
    if isinstance(x1, (int, float)) and isinstance(y1, (int, float)) and isinstance(x2, (int, float)) and isinstance(y2, (int, float)):
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        print("直角坐标系中两点的距离是", d)
        return d
    else:
        print("请在函数中输入两点坐标的数值！")
Distance(1, 2.5, -3, -4.99)
Distance(1, 2.5, -3, "ll")

st = {'a', 'b', 'c'}
def letter_set(s):
    if set(s) & st == set():
        print('字符串不包含指定集合中的字母。')
    else:
        print('字符串包含指定集合中的字母。')
letter_set('apple')
letter_set('foot')
letter_set('carbon')
