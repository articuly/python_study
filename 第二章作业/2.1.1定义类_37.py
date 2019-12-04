# coding:utf-8
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.duty = 'study something.'

    def learn(self, *sth):
        many_thing = ', '.join(sth)
        print('{0} is learning {1}.'.format(self.name, many_thing))

    def get_age(self):
        return 'The student is {0} years old.'.format(self.age)

    def get_name(self):
        return 'A student was called {0}.'.format(self.name)


s = Student('Sam', 18)
s.learn('math', 'python', 'SQL')
print(s.get_age())
print(s.get_name())
print(s.duty)
