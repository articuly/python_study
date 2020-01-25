# coding:utf-8
import sys


class MyString:
    def __init__(self):
        print('initial...')

    def getString(self):
        print('运行时输入的参数是：', sys.argv[1:])
        self.lst = sys.argv[1:]

    def printString(self):
        if len(self.lst) == 1:
            sys.stdout.write(sys.argv[1].upper())
        else:
            new_lst = []
            for i in self.lst:
                new_lst.append(i.upper())
            print('以大写形式输出其中的字母：', new_lst)


a = MyString()
a.getString()
a.printString()
