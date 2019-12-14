# coding:utf-8
# 编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    from functools import reduce
    a = reduce((lambda x, y: x * y), L)
    return a


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
