# coding:utf-8
class SchoolKid:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
        return "Name has change to {0}.".format(self.name)

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age
        return 'Age has change to {0}.'.format(self.age)


class ExaggeratngKid(SchoolKid):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_age(self):
        return '{0} has grown up to {1}.'.format(self.name, self.age + 2)


a = SchoolKid('Tom', 10)
print(a.get_name())
print(a.get_age())
print(a.set_name('Tomy'))
print(a.set_age(11))
b = ExaggeratngKid('Sam', 12)
print(b.get_name())
print(b.get_age())
