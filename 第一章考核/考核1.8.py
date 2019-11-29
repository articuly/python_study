# coding:utf-8
lst = [1, 'a', 2, 'b', 3, 'c', 4, 'd']
# 取出相应的元素放到两个元组
key = (lst[0::2])
value = (lst[1::2])
# 创建字典
d = {k: v for k, v in zip(key, value)}
print(d)
