# coding:utf-8
import re

s1 = 'This is a book. This is a book. This is an apple. This is an apple.'
s2 = re.sub(r' a | an ', ' one ', s1)
print(s2)
