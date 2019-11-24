# coding:utf-8
import random

a = random.randint(1, 100)
b = ''
c = 0
while a != b:
    b = (input("请输入100以内的正整数，看看有没有猜中随机数："))
    c = c + 1
    if b.isdigit():
        b = int(b)
        if b == a:
            print("恭喜你，用了" + str(c) + "次机会，猜中了随机数" + str(a))
        elif b > a:
            print("你猜的数字比随机数大。")
        else:
            print("你猜的数字比随机数小。")
    else:
        print("温馨提示：随机数是100以内的正整数。")
print("猜数字游戏结束。")
