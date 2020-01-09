# coding:utf-8
import random


def bubble_sort(lst):
    max_index = len(lst)
    t = 0
    for i in range(max_index):
        for j in range(max_index - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                t += 1
                print('turn {3}, i= {0} : {1} =>{2}'.format(i, j, lst, t))
    return lst


lst = [random.randint(1, 100) for i in range(10)]
print('random list:', lst)
print('sorted list:', bubble_sort(lst))
# 时间复杂度为n*(n-1)/2，约O(n**2)
