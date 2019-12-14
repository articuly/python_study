# coding:utf-8
# 编写一元二次函数y=ax^2+bx+c
def parabola(a, b, c):
    def para(x):
        w = a * x * x + b * x + c
        print('first is', w)
        return w
    print('second is ', para)
    return para


y = parabola(2, 3, 4)
r = y(3)
print('outcome is', r)


# 理解嵌套函数调用顺序
def cde():
    def fgab():
        print('sing pitch fgab')
    print("sing pitch cde")
    return fgab


c4 = cde()
c4()
