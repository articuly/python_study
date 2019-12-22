# coding:utf-8
# 列表：lst = [6, 2, 4, 10, 9, 3]，将其中最大值与列表中最后一个值互换位置，将最小值与类表中最前面一个值互换位置
# 最终得到：[2, 6, 4, 3, 9, 10]
lst = [6, 2, 4, 10, 9, 3]
a, b = min(lst), max(lst)
print(a, b)
print(lst.index(a), lst.index(b))
c, d = lst[0], lst[-1]
lst[lst.index(a)], lst[lst.index(b)] = lst[0], lst[-1]
lst[0], lst[-1] = a, b
print(lst)


def changelist(lst):
    a, b = min(lst), max(lst)
    lst[lst.index(a)], lst[lst.index(b)] = lst[0], lst[-1]
    lst[0], lst[-1] = a, b
    return lst


cl = changelist([4, 9, 12, 0, 8, 15, 3, 11, 7, 9])
print(cl)
