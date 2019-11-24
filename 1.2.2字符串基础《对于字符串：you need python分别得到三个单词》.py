# coding:utf-8
s = "you need python"
# 用字符串切片方法分别得到三个单词
print(s[:3])
print(s[4:8])
print(s[9:])
# 从左到右，隔一字符取一个
print(s[::2])
# 从右到左，隔一字符取一个
print(s[::-2])
# 字符串反序
print(s[::-1])
# 用字符串方法得到三个单词
print(s.split(" "))
