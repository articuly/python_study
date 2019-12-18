# coding:utf-8
import random


def selection_sort(lst):
    max_index = len(lst)
    t = 0
    for i in range(max_index):
        min_index = i
        for j in range(i + 1, max_index):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            t += 1
            print('turn {3}, min_index= {0}, so {1} <=> {2}'.format(min_index, lst[min_index], lst[i], t))
            lst[i], lst[min_index] = lst[min_index], lst[i]
            print(lst)
            print('-' * 50)
    return lst


lst = [random.randint(1, 100) for i in range(10)]
print('random list:', lst)
print('sorted list:', selection_sort(lst))
# 时间复杂度为n*(n-1)/2，约O(n**2)
