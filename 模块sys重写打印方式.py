# coding:utf-8
import sys


class Rewrite:
    def __init__(self, stdout):
        self.stdout = stdout

    def write(self, s):
        self.stdout.write(s.lower())


old_stdout = sys.stdout
sys.stdout = Rewrite(sys.stdout)
print(sys.stdout)
print("I LOVE PYTHON AND CODING IS COOL.")
sys.stdout = old_stdout
print("You Raise Me Up.")
