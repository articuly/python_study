# coding:utf-8
import random


# 方法一，使用冒泡排序法
def bubble_sort(lst):
    max_index = len(lst)
    for i in range(max_index):
        for j in range(max_index - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


lst = [random.randint(0, 100) for i in range(10)]
lst1, lst2, lst3 = [], [], []
for i in lst:
    if 0 <= i <= 15:
        lst1.append(i)
    elif 25 <= i <= 50:
        lst2.append(i)
    elif 60 <= i <= 100:
        lst3.append(i)
    else:
        continue
print('random list:', lst)
print('sorted list:', bubble_sort(lst1) + bubble_sort(lst2) + bubble_sort(lst3))


# 方法二，使用合并排序法
def my_range(n):
    if n in range(0, 16) or n in range(25, 51) or n in range(60, 101):
        return True
    else:
        return False


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left_lst = []
    right_lst = []
    for i in lst[:middle]:
        if my_range(i):
            if i <= lst[middle]:
                left_lst.append(i)
            else:
                right_lst.append(i)
        else:
            continue
    for i in lst[middle + 1:]:
        if my_range(i):
            if i <= lst[middle]:
                left_lst.append(i)
            else:
                right_lst.append(i)
        else:
            continue
    return merge_sort(left_lst) + [lst[middle]] + merge_sort(right_lst)


lst4 = [random.randint(0, 100) for i in range(10)]
print('random list:', lst4)
print('sorted list:', merge_sort(lst4))
