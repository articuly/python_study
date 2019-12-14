# coding:utf-8
names=['py10,py','py2.py','py1.py','py14,py']
names.sort()
print(names)
import re
def select_numbers(s):
    p= re.compile(r'(\d+)').split(s)
    print(p)
    p[1::2]=map(int,p[1::2])
    print(p[1::2])
    return p
def sort_filename(f):
    return  sorted(f,key=select_numbers)
result=sort_filename(names)
print(result)