# coding:utf-8
s = input('请输入一些语句：')
s = s.lower()
s1 = s.split(',')
s2 = sorted(s1)
for i in s2:
    print(i, end=',')
