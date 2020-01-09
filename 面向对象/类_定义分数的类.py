# coding:utf-8
class Fraction:
    def __init__(self, numerator, denominator):
        try:
            numerator / denominator
            self.numerator = numerator
            self.denominator = denominator
        except TypeError:
            print('分子、分母两个参数为数值。')

    def __str__(self):
        return '{0}/{1}'.format(int(self.numerator), int(self.denominator))

    __repr__ = __str__

    def set_frac(self, n, d):
        try:
            n / d
            self.numerator, self.denominator = n, d
        except TypeError:
            print('分子，分母两个参数为数值。')

    @staticmethod
    def gcd(x, y):  # 最大公约数，辗转相除法
        if not x > y:
            x, y = y, x
        while y != 0:
            remainder = x % y
            x, y = y, remainder
        return x

    @staticmethod  # 最小公倍数
    def lcm(x, y):
        return x * y / Fraction.gcd(x, y)

    def __add__(self, other):
        lcm_num = Fraction.lcm(self.denominator, other.denominator)
        sum_numerator = (lcm_num / self.denominator * self.numerator) + (lcm_num / other.denominator * other.denominator / lcm_num)
        return Fraction(sum_numerator, lcm_num)


a = Fraction(3, 2)
print(a)
a.set_frac(2, 3)
print(a)
b = Fraction(4, 'l')
c = Fraction(1, 2)
print(c)
print(a + c)
