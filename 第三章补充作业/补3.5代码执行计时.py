# coding:utf-8
import time


def timer(func):
    def wrapper(x):
        with open('logtimer.txt', mode='a') as f:
            start = time.time()
            func(x)
            end = time.time()
            f.write('func run {0}s\n'.format(end - start))
        return func(x)

    return wrapper


@timer
def func(x):
    lst = []
    for n in range(2, x):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            lst.append(n)
    return lst


print(func(100))
print(func(1000))
print(func(10000))
# print(func(100000))
