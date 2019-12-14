# coding:utf-8
lst = []
for n in range(2, 50):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', int(n / x))
            break
    else:
        lst.append(n)
print(lst, 'are prime numbers')


def find_prime(p):
    lst = []
    for n in range(2, p):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            lst.append(n)
    print(lst)
    return lst


find_prime(100)
