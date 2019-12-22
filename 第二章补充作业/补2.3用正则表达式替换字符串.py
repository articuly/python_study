# coding:utf-8
import re

s1 = 'This is a book. This is a book. This is an apple. This is an apple.'
s2 = re.sub(r' a | an ', ' one ', s1)
print(s2)

import re


# 1
def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]

    return rx.sub(one_xlat, text)


# 2
class make_xlat:
    def __init__(self, *args, **kwargs):
        self.adict = dict(*args, **kwargs)
        self.rx = self.make_rx()

    def make_rx(self):
        return re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(self, match):
        return self.adict[match.group(0)]

    def __call__(self, text):
        return self.rx.sub(self.one_xlat, text)


if __name__ == "__main__":
    text = "It is a good person."
    adict = {"a good": "ONE", 'person': "human"}
    rp = make_xlat(adict)
    r = rp(text)
    print(r)
    # r = multiple_replace(text, adict)
    # print(text)
    # print(r)
