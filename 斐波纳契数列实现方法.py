# coding:utf-8


# 用常规函数的方法
def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        lst = [0, 1]
        [lst.append(lst[-1] + lst[-2]) for i in range(n - 2)]
        return lst


print(fib(10))


# 用迭代器的方法
class Fibs:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fi = self.a
        if fi > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fi


fibs = Fibs(1000)
fib_lst = [next(fibs) for i in range(10)]
print(fib_lst)


# 用递归的方法
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


fibo_lst = [fibo(i) for i in range(10)]
print(fibo_lst)
