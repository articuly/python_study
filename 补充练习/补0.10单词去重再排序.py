# coding:utf-8
s = input('请输入一些语句：')
s = s.lower()
s1 = set(s.split(' '))
s2 = sorted(list(s1))
print(s2)
