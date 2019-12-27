# coding:utf-8
import collections

fd = collections.deque([1, 2, 3], maxlen=3)
print(fd)
fd.appendleft(4)
print(fd)
fd.append(5)
print(fd)
