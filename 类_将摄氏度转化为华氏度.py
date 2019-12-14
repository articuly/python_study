# coding:utf-8
class Celsius:
    def __init__(self, temp=0.0):
        self.__temp = temp

    def to_fahrenheit(self):
        return (self.__temp * 1.8) + 32

    @property
    def temperature(self):
        print('Getting value.')
        return self.__temp

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError('Temperature below -273.15 is not possible.')
        print('Setting value.')
        self.__temp = value


c=Celsius(-12)
print(c.__dict__)
print(c.temperature)
print(c.to_fahrenheit())
c.__temperature=-300
print(c.__dict__)

# 方法二
# class Celsius:
#     def __init__(self, temperature=0.0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.__temperature * 1.8) + 32
#
#     def get_temperature(self):
#         print('Getting value.')
#         return self.__temperature
#
#     def set_temperature(self, value):
#         if value < -273.15:
#             raise ValueError('Temperature below -273.15 is not possible.')
#         print('Setting value.')
#         self.__temperature = value
#
#     temperature = property(get_temperature, set_temperature)
#
#
# d = Celsius(-300)
# e = Celsius(12)
# print(e.to_fahrenheit())
