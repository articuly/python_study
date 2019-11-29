# coding:utf-8
skills = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
mySkills = {'Python', 'R', 'C'}
i = mySkills & skills
if i == mySkills:
    print("你所掌握的技术在技术栈范围内")
elif i == set():
    print("你所掌握的技术全都不在技术栈范围内")
else:
    a = '、 '.join(i)
    print("你所掌握的{0}技术在技术栈范围内".format(a))
