# coding:utf-8
class Temperature:
    def __init__(self, degree, unit='C'):
        self.degree = degree
        self.unit = unit
        if self.unit not in ('C', 'F', 'K'):  # 温度单位必须在使用范围内
            raise ValueError('温度单位必须是C（摄氏度）、F（华氏度）和K（开尔文）')
        if self.degree < -273.15 and self.unit == 'C':
            raise ValueError('宇宙不存在低于零下273.15摄氏度的温度')
        if self.degree < 0 and self.unit == 'K':
            raise ValueError('宇宙不存在低于零开尔文的温度')
        if self.degree < -459.67 and self.unit == 'F':
            raise ValueError('宇宙不存在低于零下459.67华氏度的温度')

    @property
    def temperature(self):
        print('现在温度是{0} {1}'.format(self.degree, self.unit))
        return self.degree, self.unit

    @temperature.setter
    def temperature(self, degree):
        if degree < -273.15 and self.unit == 'C':
            raise ValueError('宇宙不存在低于零下273.15摄氏度的温度')
        if degree < 0 and self.unit == 'K':
            raise ValueError('宇宙不存在低于零开尔文的温度')
        if degree < -459.67 and self.unit == 'F':
            raise ValueError('宇宙不存在低于零下459.67华氏度的温度')
        self.degree = degree
        print('现在温度变成{0} {1}'.format(self.degree, self.unit))

    # 转换为华氏度温度
    def to_fahrenheit(self):
        if self.unit == 'C':
            self.degree = self.degree * 1.8 + 32
        if self.unit == 'K':
            self.degree = self.degree * 1.8 - 459.67
        self.unit = 'F'
        print('现在温度是{0:.2f}华氏度'.format(self.degree))
        return self.degree, self.unit

    # 转换为开尔文温度
    def to_kelvin(self):
        if self.unit == 'C':
            self.degree = self.degree + 273.15
        if self.unit == 'F':
            self.degree = (self.degree + 459.67) * 5 / 9
        self.unit = 'K'
        print('现在温度是{0:.2f}开尔文'.format(self.degree))
        return self.degree, self.unit

    # 转换为摄氏度温度
    def to_celsius(self):
        if self.unit == 'K':
            self.degree = self.degree - 273.15
        if self.unit == 'F':
            self.degree = (self.degree - 32) * 5 / 9
        self.unit = 'C'
        print('现在温度是{0:.2f}摄氏度'.format(self.degree))
        return self.degree, self.unit


a = Temperature(911, 'F')
a.temperature
a.temperature = 9
a.to_kelvin()
a.to_celsius()
# a.temperature=-500
print('------')
b = Temperature(300, 'K')
b.temperature
# b.temperature=-10
b.to_fahrenheit()
b.to_celsius()
print('------')
c = Temperature(12)
c.temperature
c.to_fahrenheit()
c.to_kelvin()
print('------')
# d = Temperature(15,'A')

# 补充方法
class Temperature:
    coefficient = {"c": (1.0, 0.0, -273.15), "f": (1.8, -273.15, 32.0)}

    def __init__(self, **kargs):
        assert set(kargs.keys()).intersection("kfcKFC"), "invalid arguments {0}".format(kargs)  # 断言单位在给定范围
        name, value = kargs.popitem()  # 返回并删除字典中的最后一对键和值
        name = name.lower()
        setattr(self, name, float(value))

    def __getattr__(self, name):
        try:
            eq = self.coefficient[name.lower()]
        except KeyError:
            raise AttributeError(name)
        return (self.k + eq[1]) * eq[0] + eq[2]

    def __setattr__(self, name, value):
        name = name.lower()
        if name in self.coefficient:
            eq = self.coefficient[name]
            self.k = (value - eq[2]) / eq[0] - eq[1]
        elif name == 'k':
            object.__setattr__(self, name, value)
        else:
            raise AttributeError(name)

    def __str__(self):
        return "{0}K".format(self.k)

    def __repr__(self):
        return "Temperature(K={0}".format(self.k)


t = Temperature(c=64)
print("c=64, f=", t.f)
t.f = 23
print("f=23, c=", t.c)
