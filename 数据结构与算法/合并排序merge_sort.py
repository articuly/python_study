# coding:utf-8
import random


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left_lst = []
    right_lst = []
    for i in lst[:middle]:
        if i <= lst[middle]:
            left_lst.append(i)
        else:
            right_lst.append(i)
    for i in lst[middle + 1:]:
        if i <= lst[middle]:
            left_lst.append(i)
        else:
            right_lst.append(i)
    print(left_lst, [lst[middle]], right_lst)
    return merge_sort(left_lst) + [lst[middle]] + merge_sort(right_lst)


lst = [random.randint(1, 100) for i in range(10)]
print('random list:', lst)
print('sorted list:', merge_sort(lst))
'''
每次分割成2部分，大概log2n次可以得到一个元素
合并次是O(n)
平均水平是O(nlog2n)
由于使用了递归和两个列表，所以以空间复杂度增大O(n)+O(logn)
'''
