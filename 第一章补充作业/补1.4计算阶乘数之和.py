# coding:utf-8
def factorial(n):
    a = 1
    for i in range(1, n + 1):
        a = a * i
    return a


print(factorial(5))
lst = [factorial(i) for i in range(1, 11)]
print(sum(lst))


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * fact(n - 1))


print(sum([fact(i) for i in range(1, 16)]))


# 补充方法
def func(n):
    s, t = 0, 1
    for n in range(1, n + 1):
        t *= n
        s += t
    return s


print(func(10))
