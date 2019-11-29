# coding:utf-8
s1 = "python"
s2 = "rust"
# 将字符串转化为列表
lst = list(s1)
print(lst)
# 将“rust”每个字母追加到列表
lst.extend(s2)
# lst = lst + list(s2)
print(lst)
# 对列表进行排序
lst.sort()
print(lst)
# 删除列表重复的元素
print(list(set(lst)))
