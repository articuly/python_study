# coding:utf-8
# 字符串可能包含若干个数字、字母、空格或者其他符号
# 分别统计其中的各类符号，即英文字母、空格、数字和其他符号的个数
def diff(s):
    s = str(s)
    a = b = c = d = 0
    for i in s:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            b += 1
        elif i.isspace():
            c += 1
        else:
            d += 1
    print("英文字母个数是", a)
    print("数字个数是", b)
    print("空格个数是", c)
    print("其它符号个数是", d)
    return a, b, c, d


x = diff("abc1234     ????//")
print(x)
diff('asdf684  18e/在,.f1 1e5g7 d1')
