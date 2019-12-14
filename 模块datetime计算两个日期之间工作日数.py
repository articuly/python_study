# coding:utf-8
# 不考虑国家法定节日的情况
import datetime


def new_day(yyyy, mm, dd):
    return datetime.date(yyyy, mm, dd)


def old_day(yyyy, mm, dd):
    return datetime.date(yyyy, mm, dd)


def work_days(new_day, old_day):
    delta = (new_day - old_day).days
    works = 0
    if old_day.isoweekday() >= 6:
        works = works + 0
    else:
        works = works + (6 - old_day.isoweekday())
    if new_day.isoweekday() <= 5:
        works = works + new_day.isoweekday()
    else:
        works = works + 5
    weeks = (delta - (7 - old_day.isoweekday()) - new_day.isoweekday()) / 7
    work_day = works + weeks * 5
    return delta, works, work_day


a = new_day(2019, 12, 6)
b = old_day(2019, 5, 9)
z = work_days(a, b)
print(z)
