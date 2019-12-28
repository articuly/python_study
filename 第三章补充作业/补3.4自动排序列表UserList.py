# coding:utf-8
from collections import UserList


class Sorted_List(UserList):
    def __init__(self, *initlist):
        for i in initlist:
            if isinstance(i, int):
                initlist = sorted(initlist)
                super().__init__(initlist)
            else:
                raise TypeError('data must be int')

    def append(self, item):
        if isinstance(item, int):
            super().append(item)
            return self.sort()
        else:
            raise TypeError('data must be int')


sl = Sorted_List(5, 2, 7)
print(sl)
sl.append(1)
print(sl)
sl.append(3)
print(sl)
# sl.append('e')
