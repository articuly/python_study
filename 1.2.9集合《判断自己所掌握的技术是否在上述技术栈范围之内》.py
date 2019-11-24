# coding:utf-8
skills = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
mySkills = {'Python', 'R'}
a = mySkills.intersection(skills)
if a == mySkills:
    print("你所掌握的技术在技术栈范围内")
elif a == set():
    print("你所掌握的技术全都不在技术栈范围内")
else:
    print("你所掌握的", a, "技术在技术栈范围内")
