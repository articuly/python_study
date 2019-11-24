# coding:utf-8
# 根据大写小写的参数，转化单词
# 方法一
def upper(x):
    if str(x).isalpha():
        u = str(x).upper()
        print(u)
        return u
    else:
        print("请输入一个英文单词")
        return
def lower(x):
    if str(x).isalpha():
        l = str(x).lower()
        print(l)
        return l
    else:
        print("请输入一个英文单词")
        return
def change(x, func):
    c = func(x)
    return c
change('apple', upper)
change('Http', lower)


# 方法二
def convert(x, lower=True):
    if lower is True:
        print(x.lower())
        return x.lower()
    elif lower is False:
        print(x.upper())
        return x.upper()
    else:
        print("请输入lower的正确参数")
        return x
convert('table')
convert('table', lower=False)
convert('ONE', lower=True)
convert('ONE', lower='OK')
