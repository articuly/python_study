# coding:utf-8
from collections.abc import Iterable


def fatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from fatten(x)
        else:
            yield x


lst = [1, 2, [3, 4, [5, 6], 7], 8, 9]
print(fatten(lst))
print(list(fatten(lst)))
