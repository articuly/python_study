# coding:utf-8
# lambda, map(), filter()的作用
lst1 = [i + 1 for i in range(0, 10)]
print(lst1)
lst2 = [(lambda x: x + 1)(i) for i in range(0, 10)]
print(lst2)
lst3 = map(lambda x: x + 1, range(0, 10))
print(list(lst3))
lst4 = [i for i in range(-5, 5) if i > 0]
print(lst4)
lst5 = filter(lambda x: x > 0, range(-5, 5))
print(list(lst5))
