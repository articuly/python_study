# coding:utf-8
from itertools import count
from itertools import cycle
from itertools import islice

counter = count(start=13)
next(counter)
next(counter)

colors = cycle(['red', 'white', 'blue'])
next(colors)
next(colors)

color=islice(colors,0,20)
for x in color:
    print(x)