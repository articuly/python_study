# coding:utf-8
# 用列表的方法打印九九乘法口诀
for b in range(1, 10):
    lst = []
    for a in range(1, b + 1):
        lst.append('{0} X {1} = {2}'.format(a, b, a * b))
    print(lst)
