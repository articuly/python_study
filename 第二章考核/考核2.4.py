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


# 补充方法
class Physicist:
    def __init__(self, name, iq=120, looks='handsom', subject='physics'):
        self.name = name
        self.iq = iq
        self.looks = looks
        self.subject = subject

    def research(self, field):
        print("{0} research {1}".format(self.name, field))

    def speak(self):
        print("My name is", self.name)
        print("I am", self.looks)
        print("Intelligence is", self.iq)
        print("I like", self.subject)


class ExperimentalPhysicist(Physicist):
    def __init__(self, main_study, name, iq=120, looks='handsom', subject='physics'):
        self.main_study = main_study
        super().__init__(name, iq, looks, subject)

    def experiment(self):
        print("{0} is in Physics Lab.".format(self.name))


class TheoreticalPhysicist(Physicist):
    def __init__(self, theory, name, iq=120, looks='handsom', subject='physics'):
        self.theory = theory
        super().__init__(name, iq, looks, subject)

    def research(self, field, base):
        super().research(field)
        print("My theory is {0}, it is based on {1}".format(self.theory, base))


einstein = TheoreticalPhysicist('Relativity', 'Albert Einstein', iq=160, looks='Hair is messy but handsome')
einstein.research('Black Hole', 'General relativity')
einstein.speak()
print("*" * 20)
wu = ExperimentalPhysicist('Nuclear Physics', 'Chien-Shiung Wu', 160, 'beautiful and wisdom')
wu.experiment()
wu.speak()
