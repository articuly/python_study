# coding:utf-8
def recursion_sum(min, max):
    if min > max:
        return 0
    else:
        return min + recursion_sum(min + 1, max)


# 本机最大递归深度是2983

a = recursion_sum(1, 1000)
print(a)
