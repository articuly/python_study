# coding:utf-8
import sys


class MyString:
    def __init__(self, stdout):
        self.stdout = stdout

    def getString(self,t):
        self.t = sys.argv[1]

    def printString(self,s):
        self.stdout.write(s.upper())


sys.stdout = MyString(sys.stdout)
# print(MyString.getString(sys.argv[1])
