# coding:utf-8
import random


def insertion_sort(lst):
    # t = 0
    for i in range(1, len(lst)):
        item_to_insert = lst[i]  # 准备拿去插入的元素
        for j in range(i - 1, -2, -1):  # 与前面项进行比较，直到自己跟自己比完确定是最小的值
            if item_to_insert < lst[j]:
                lst[j + 1] = lst[j]  # 小于则后移
                # t += 1
                # print('turn {0}, {1}'.format(t, lst))
            else:
                break
        lst[j + 1] = item_to_insert
        # t += 1
        # print('turn {0}, {1}'.format(t, lst))
    return lst


lst = [random.randint(1, 100) for i in range(10)]
print('random list:', lst)
print('sorted list:', insertion_sort(lst))
# 时间复杂度为n*(n-1)/2，约O(n**2)