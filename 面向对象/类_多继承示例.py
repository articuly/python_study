# coding:utf-8
import random


class Father:
    def __init__(self):
        self.fa_chromosome = 'XY'

    def Father_do(self):
        return 'Lead the family.'


class Mother:
    def __init__(self):
        self.mo_chromosome = 'XX'

    def Mother_do(self):
        return 'Care the family.'


class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def gender(self):
        fa = random.choice(self.fa_chromosome)
        mo = random.choice(self.mo_chromosome)
        print('father:', fa, '&', 'mother:', mo)
        ch_gender = fa + mo
        if 'Y' in ch_gender:
            print('he is a boy.')
            return 1
        else:
            print('she is a girl.')
            return 0


a = Child()
a.gender()
print(a.__dict__)
