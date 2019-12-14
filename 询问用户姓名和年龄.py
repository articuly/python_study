# coding:utf-8
# 可以加入isdigit的判断
n = input("您叫什么名字？")
a = input("您现在多大了？")
b = str(int(a) + 10)
print(n + "现在" + a + "岁，10年后是" + b + "岁。")
print("您的名字是{0}\n现在是{1}岁\n10年后是{2}岁".format(n, a, b))
