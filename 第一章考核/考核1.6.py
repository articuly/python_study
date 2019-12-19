# coding:utf-8
# 实现正整数阶乘的函数
def func(n):
    try:
        if n > 0:
            s = 1
            for i in range(1, n + 1):
                s = s * i
            return s
        else:
            return '函数参数必须是正整数。'
    except TypeError:
        return '函数参数必须是正整数。'


a = func(10)
print(a)
b = func(-1)
print(b)
c = func('abc')
print(c)


# 补充方法
def fact(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


d = fact(10)
print(d)
