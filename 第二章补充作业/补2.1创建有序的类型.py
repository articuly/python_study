# coding:utf-8
import collections.abc
import bisect


class Sortion(collections.abc.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


a = Sortion([5, 6, 7, 1, 3, 12, 7, 2])
print(list(a))
b = Sortion((5, 6, 7, 1, 3, 12, 7, 2))
print(tuple(b))
print(b)
c = Sortion({'a': 1, 'd': 10, 'k': 2, 'z': 8, 'f': 6})
print(list(c))
print(len(a))
print(b[4])
c.add('g')
print(list(c))
