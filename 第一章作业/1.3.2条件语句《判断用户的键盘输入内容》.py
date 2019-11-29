# coding:utf-8
a = input("请输入一些内容：")
if "." in a:  # 处理输入内容带小数点的情况
    lst = a.split(".")
    if lst[0].isdigit() and lst[1].isdigit():  # 小数点前后都是数字的情况“XXX.XXX”
        print(float(a) * 10)
    elif lst[0].isdigit() and lst[1] == '':  # 小数点前输入了数字，后面没有继续输入的情况“XXX.”
        print(int(lst[0]) * 10)
    elif lst[0] == '' and lst[1].isdigit():  # 小数点没有输入数字，后面为数字的情况“.XXX”
        print(float("0." + lst[1]) * 10)
    else:  # 其它情况
        print(a)
elif a.isdigit():  # 输入内容全为数字的情况
    print(int(a) * 10)
elif a.isalpha():  # 输入内容全为字母的情况
    print(a + "@python")
else:  # 其它情况
    print(a)
