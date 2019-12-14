import math, random


def ad(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(0, 100))
        s = sum(lst)
        a = s / n
    for i in range(n):
        dv = pow((lst[i] - a), 2)
        sdv = math.sqrt(dv / n)
    return a, sdv


print(ad(10000))
