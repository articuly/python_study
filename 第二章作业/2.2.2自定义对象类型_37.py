# coding:utf-8
class Rectangle:
    def __init__(self):
        self.width = 0
        self.length = 0

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.length
        else:
            raise AttributeError('没有找到{0}属性'.format(name))

    def __setattr__(self, name, value):
        try:
            if name == 'size':
                self.width, self.length = map(abs, value)
            else:
                self.__dict__[name] = abs(value)
        except TypeError:
            print('size属性需要两个正数作为参数。')


rect = Rectangle()
rect.width = 3
rect.length = 4
print(rect.size)
print('------')
rect.size = 30, -40
print(rect.width)
print(rect.length)
print(rect.height)
