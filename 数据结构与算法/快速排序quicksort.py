# coding:utf-8
import random


def quicksort(lst):
    quicksort_helper(lst, 0, len(lst) - 1)
    return lst


def quicksort_helper(lst, left, right):
    print('left: {0}, right: {1}'.format(left, right))
    if left < right:
        boundary = partition(lst, left, right)
        quicksort_helper(lst, left, boundary - 1)
        quicksort_helper(lst, boundary + 1, right)


def partition(lst, left, right):
    middle = (left + right) // 2
    lst[right], lst[middle] = lst[middle], lst[right]
    boundary = left
    for i in range(left, right):
        print(lst)
        if lst[i] < lst[right]:
            lst[i], lst[boundary] = lst[boundary], lst[i]
            # print('boundary: {0}'.format(boundary))
            boundary += 1
    lst[right], lst[boundary] = lst[boundary], lst[right]
    return boundary


lst = [random.randint(1, 100) for i in range(10)]
print('random list:', lst)
print('sorted list:', quicksort(lst))
'''
第一次是O(n)
每次分割成2部分，大概log2n次可以得到一个元素
最好的水平是O(nlog2n)
最坏的是每个元素都作为一次分割点，O(n**2)
'''