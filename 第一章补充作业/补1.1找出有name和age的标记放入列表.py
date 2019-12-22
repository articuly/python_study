# coding:utf-8
records = [("age", 20, "00"), ("age", 28, "92"), ("name", "Newton"), ("name", "Maxwell"), ("age", 30, "90")]
age_list = []
name_list = []
for item in records:
    if 'age' in item:
        age_list.append(item)
    elif 'name' in item:
        name_list.append(item)
    else:
        pass

print(age_list)
print(name_list)

# 补充方法
age_lst = []
name_lst = []
for tag, *tags in records:  # ①
    if tag == "age":
        age_lst.append(tags)
    elif tag == "name":
        name_lst.append(tags)

print(age_lst)
print(name_lst)
