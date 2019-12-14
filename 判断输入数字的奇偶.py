# coding:utf-8
# 判断输入数字是奇数还是偶数
a = input("请输入一个整数：")
if a.isdigit():
    if int(a) % 2 == 0:
        print(a, "是偶数")
    else:
        print(a, "是奇数")
else:
    print("输入有误，下次请输入一个整数。")
