# coding:utf-8
import itertools


def permute_and_combine(args):
    for i in itertools.permutations(args, 3):
        print(i, end=' ')
    print('\n')
    for i in itertools.permutations(args, 2):
        print(i, end=' ')
    print('\n')
    for i in itertools.combinations(args, 3):
        print(i, end=' ')
    print('\n')
    for i in itertools.combinations(args, 2):
        print(i, end=' ')


lst = ['a', 'b', 'c']
permute_and_combine(lst)
