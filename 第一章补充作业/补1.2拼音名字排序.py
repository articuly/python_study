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
