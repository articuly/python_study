# coding:utf-8
class Human:
    def __init__(self, name, age):  # 初始化两个参数
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(Human):  # 继承父类Human
    def __init__(self, school, name, age):
        self.school = school
        super().__init__(name, age)  # 雇用父类的方法

    def grade(self, n):
        print('{0} is at the age of {1}, and is {2} grade in {3}'.format(self.name, self.age, n, self.school))
        # n不属于实例的属性，属于方法的参数，所以不能用self.n传递


a = Student('JNU', 'LSL', 19)
a.grade(13)
print(type(a))
print(type(Student))
print(type(Human))
print(a.get_age())
print(a.get_name())
print(a)
print(Student)
print(a.__dict__)
