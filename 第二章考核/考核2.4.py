# coding:utf-8
class Physicist:
    def __init__(self, name):
        self.name = name
        print('{0}是一位物理学家。'.format(self.name))

    def who(self):
        print('{0}是探索物质世界的组成和运行规律的科学家。'.format(self.name))


class Theoretical_physicist(Physicist):
    def __init__(self, name):
        self.name = name
        print('{0}是一位理论物理学家。'.format(self.name))

    def job(self):
        print('{0}的工作是为现实世界建立数学模型来试图理解所有物理现象的运行机制。'.format(self.name))


class Experimental_physicist(Physicist):
    def __init__(self, name):
        self.name = name
        print('{0}是一位实验物理学家。'.format(self.name))

    def job(self):
        print('{0}的工作是直接观察物理现象，获取关于宇宙中从大到小各种资料，并解释所得到的数据资料。'.format(self.name))


a = Physicist('牛顿')
b = Experimental_physicist('特斯拉')
c = Experimental_physicist('法拉第')
d = Theoretical_physicist('爱因斯坦')
e = Theoretical_physicist('杨振宁')
a.who()
b.job()
c.who()
d.job()
e.who()
