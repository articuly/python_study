# coding:utf-8
lst = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        lst.append(i)
        print(i, end=', ')

print('\n------------')
lst2 = [i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0]
for i in lst2:
    int(i)
    print(i, end=', ')
