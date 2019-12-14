# coding:utf-8
from enum import Enum, unique


class Gender(Enum):
    Male = 1
    Female = 2


class Student:
    def __init__(self, name, gender):
        self.name = name
        if isinstance(gender, Gender):
            self.gender = gender
        else:
            raise ValueError('gender must be Male(1) or Female(2).')


# 测试:
print(type(Gender))
print(type(Student))
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
