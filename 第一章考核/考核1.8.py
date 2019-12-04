# coding:utf-8
lst = [1, 'a', 2, 'b', 3, 'c', 4, 'd']
# 取出相应的元素放到两个元组
key = (lst[0::2])
value = (lst[1::2])
# 创建字典
d1 = {k: v for k, v in zip(key, value)}
d2 = dict(zip(key, value))
print(d1)
print(d2)


# 补充方法
def dct_from_seq(seq):
    return dict(zip(seq[::2], seq[1::2]))


lst = [1, "a", 2, "b", 3, "c", 4, "d"]
dct = dct_from_seq(lst)
print(dct)
