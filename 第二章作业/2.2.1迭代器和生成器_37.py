# coding:utf-8
# 用(i for i in iterable)方式创建生成器
def float_range(start, stop, step=1.0):
    try:
        if step > 0:
            if stop >= start:
                float_seq = ((start + step * i) for i in range(int((stop - start) / step) + 1) if
                             (start + step * i) <= stop)
                return float_seq
            else:
                return '当step为正数时，参数stop必须大于等于start'
        elif step < 0:
            if stop <= start:
                float_seq = ((start + step * i) for i in range(int((stop - start) / step) + 1) if
                             (start + step * i) >= stop)
                return float_seq  # 用(i for i in iterable)方式创建生成器并返回
            else:
                return '当step为负数时，参数stop必须小于等于start'
        else:
            return '无法创建等差数列，请将step参数设置为非零的值。'
    except TypeError:
        return '函数所有参数必须是数字。'


for a in float_range(1, 7.5, 1.2):
    print(a)
print(float_range(1.1, 8, 0))
b = float_range(-5, 5, 2.4)
print(next(b))
print(next(b))


# 用yield的方式创建生成器
def frange(start, stop=None, step=1.0):
    if stop is None:
        stop = float(start)
        start = 0.0
    if step > 0:
        while start <= stop:
            yield start
            start = start + step
    elif step < 0:
        while start >= stop:
            yield start
            start = start + step
    else:
        return '无法创建等差数列，请将step参数设置为非零的值。'


d = frange(0.6, 9.8, 1.2)
print(list(d))
e = frange(12)
print(list(e))
print(frange(22, 1.1, -1.1))
