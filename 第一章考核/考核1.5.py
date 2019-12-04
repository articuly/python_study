# coding:utf-8
def gravity(g):
    def wrapper(m):
        return m * g
    return wrapper


g, m = 9.8, 5
a = gravity(g)
b = a(m)
print("在重力加速度为{0}ms^-2的条件下，质量{1}KG的物体，其重力为{2}N".format(g, m, b))
