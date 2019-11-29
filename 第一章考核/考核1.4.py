# coding:utf-8
def float_range(start, stop, step=1):
    try:
        if step > 0:
            if stop >= start:
                float_list = [(start + step * i) for i in range(int((stop - start) / step) + 1) if
                              (start + step * i) <= stop]
                return float_list
            else:
                return '当step为正数时，参数stop必须大于等于start'
        elif step < 0:
            if stop <= start:
                float_list = [(start + step * i) for i in range(int((stop - start) / step) + 1) if
                              (start + step * i) >= stop]
                return float_list
            else:
                return '当step为负数时，参数stop必须小于等于start'
        else:
            return '无法创建等差数列，请将step参数设置为非零的值。'
    except TypeError:
        return '函数所有参数必须是数字。'


a = float_range(1, 18.5, 1.2)
print(a)
b = float_range(-5, 5, 0.9)
print(b)
c = float_range(19.6, 9.8, -1.1)
print(c)
d = float_range(1.1, 8, 0)
print(d)
e = float_range(1.2, 1.2, 0.8)
print(e)
f = float_range(1, 5)
print(f)
g = float_range('a', 'z', 1)
print(g)

