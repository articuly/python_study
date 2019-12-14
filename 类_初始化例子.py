# coding:utf-8
class SuperMan:
    """
    a class of superman.
    """
    def __init__(self, name): # 初始化方法
        print("it has been done.")
        self.name = name
        self.kongfu = 'xianglongshibazhang'
    def done(self):
        return 'coding'

s = str('twt12')
print(s)
p = SuperMan('LSL')
print(type(p))
print(p.kongfu)
print(p.name)
print(p.done())
print(p.done)
