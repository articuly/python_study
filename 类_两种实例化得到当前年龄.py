# coding:utf-8
import datetime


# 方法一
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def by_birth(cls, name, birth_year):
        this_year = datetime.date.today().year
        age = this_year - birth_year
        return cls(name, age)

    def info(self):
        return '{0} is at the age of {1}.'.format(self.name, self.age)


s = Person('Sam', 29)
print(s.info())
m = Person.by_birth('Mary', 1988)
print(m.info())


# 方法二
class Human:
    def __init__(self, name, **dct):
        self.name = name
        self.age = dct.get('age')
        self.birth = dct.get('birth')

    def get_age(self):
        if self.age:
            return self.age
        elif self.birth:
            this_year = datetime.date.today().year
            self.age = this_year - self.birth
            return self.age
        else:
            return False


z = Human('Zeta', age=18)
print(z.name, z.get_age())
w = Human('William', birth=1994)
print(w.name, w.get_age())
