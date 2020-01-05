# coding:utf-8
# 用合并排序的方法对(id, data）元组的数据列表进行排序
import random


def my_sort(lst, key='id'):
    if key == 'id' or 0:
        k = 0
        return merge_sort(lst, k)
    elif key == 'data' or 1:
        k = 1
        return merge_sort(lst, k)
    else:
        raise Exception('请输入正确排序的键')


def merge_sort(lst, k):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left_lst = []
    right_lst = []
    for i in lst[:middle]:
        if i[k] <= lst[middle][k]:
            left_lst.append(i)
        else:
            right_lst.append(i)
    for i in lst[middle + 1:]:
        if i[k] <= lst[middle][k]:
            left_lst.append(i)
        else:
            right_lst.append(i)
    return merge_sort(left_lst, k) + [lst[middle]] + merge_sort(right_lst, k)


lst1 = [random.randint(1, 100) for i in range(10)]
lst2 = list(zip(range(10), lst1))
print('random list:', lst2)
print('sorted list:', my_sort(lst2, 'data'))
lst3 = [random.randint(1, 100) for i in range(10)]
lst4 = [random.randint(1, 100) for i in range(10)]
lst5 = list(zip(lst3, lst4))
print('random list:', lst5)
print('sorted list:', my_sort(lst5, 'id'))
