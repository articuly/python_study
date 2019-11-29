# coding:utf-8
s = "Life is short You need python"
lst = s.split()
# 显示单词的小写状态
x = []
for i in lst:
    i = i.lower()
    x.append(i)
print(x)
# 用列表解析的方法显示单词的大写状态
print([y.upper() for y in lst])
# 统计每个单词的长度
for z in lst:
    print(z, "单词长度是", len(z), "个字母")
