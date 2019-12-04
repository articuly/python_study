# coding:utf-8
class Animals:
    def __init__(self, kind):
        self.kind = kind
        print('{0} can move.'.format(self.kind))


class Human(Animals):
    def __init__(self, name):
        self.name = name
        print('{0} can talk. it is done.'.format(self.name))


class Programmer(Human):
    def __init__(self, name, sth):
        super().__init__(name)  # 调用父类会执行一次init方法
        self.sth = sth
        print('{0} is coding {1}'.format(self.name, self.sth))


a = Animals('mankind')
m = Human('Bob')
b = Programmer('Bob', 'Python')
