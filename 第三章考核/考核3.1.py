# coding:utf-8
# 查找是否存在特殊字符
import re


def special_characters(s):
    if re.search(r'[^A-Za-z0-9]+', s):
        return True
    else:
        return False


s1 = 'learnpython*7%%99hello'
s2 = '123654789'
s3 = 'learnpython'
print(special_characters(s1))
print(special_characters(s2))
print(special_characters(s3))
