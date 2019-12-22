# coding:utf-8
names = ["zhang", "wang", "li", "zhao"]
alist = []
blist = []
for item in names:
    if 'a' in item:
        alist.append(item)
    else:
        blist.append(item)

sorted(alist)
print(alist)
print(blist)
alist.extend(blist)
print(alist)

# 补充方法
n = sorted(names, key=lambda x: 'a' in x, reverse=True)
print(n)
