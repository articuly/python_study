# coding:utf-8
class Countdown:
    def __init__(self, n):
        try:
            self.n = int(n)
        except ValueError:
            print('参数必须是正整数。')

    def __iter__(self):
        return self

    def __next__(self):
        count = self.n
        if count < 0:
            raise StopIteration
        self.n = self.n - 1
        return count


c = Countdown(12)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
d = Countdown('ll')


# 补充方法
class ReverseRange:
    def __init__(self, n):
        self.n = n

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        return self.n

    def __iter__(self):
        return self


for i in ReverseRange(11):
    print(i)
