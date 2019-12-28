# coding:utf-8
import heapq
import random

# 练习一
phones = [{"name": "Huawei", "count": 100, "price": 2999.9},
          {"name": "Apple", "count": 90, "price": 4999.9},
          {"name": "Xiaomi", "count": 80, "price": 3999.9}]

a = heapq.nlargest(1, phones, key=(lambda x: x['count']))
b = sorted(phones, key=(lambda x: x['count']))[-1]
print(a)
print(b)


# 练习二
def heap_sort(lst):
    heapq.heapify(lst)
    return lst


lst = [random.randint(1, 10) for i in range(10)]
print('before sorted: {0}'.format(lst))
c = heap_sort(lst)
print('after sorted: {0}'.format(c))
