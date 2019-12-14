# coding:utf-8
class Roman_numerals:
    Roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
             (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
             (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    def __init__(self, n):
        self.n = n

    # for循环，用divmod求出商和余数
    def arabic2roma(self):
        number = self.n  # 实例的n参数，传入到实例方法里的变量
        result = ''
        for (arabic, roman) in self.Roman:  # 二元变量的方式寻找类的静态属性
            (factor, number) = divmod(number, arabic)
            result = result + roman * factor  # 某些罗马数字会显示几次
        return result

a = Roman_numerals(1024)
print(a.arabic2roma())
b=Roman_numerals(12345)
print(b.arabic2roma())
print(a.__dict__)
print(dir(a))