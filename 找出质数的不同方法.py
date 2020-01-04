# coding:utf-8
#方法一
import math
def is_prime1(n): # isPrime1
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#方法二
def is_prime2(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

#方法三
from itertools import count
def is_prime3(n):
    if n <= 1:
        return False
    for i in count(2):
        if i * i > n:
            return True
        if n % i == 0:
            return False

#方法四
def is_prime4(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

#方法五
def find_prime(nlst):
    primes = []
    for n in nlst:
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            primes.append(n)
    return primes

ns = range(2, 20)
print(find_prime(ns))

primes_lst = [i for i in ns if is_prime3(i)]
print(primes_lst)
