# coding:utf-8
import datetime, calendar


def last_friday_1(today):
    last_friday = today
    one_day = datetime.timedelta(days=1)
    while last_friday.weekday() != calendar.FRIDAY:
        last_friday -= one_day
    return last_friday.strftime('%A, %Y-%m-%d')


def last_friday_2(today):
    target_day = calendar.FRIDAY
    this_day = today.weekday()
    delta = (this_day - target_day) % 7
    last_friday = today - datetime.timedelta(days=delta)
    return last_friday.strftime('%A, %Y-%m-%d')


a = last_friday_1(datetime.date.today())
print(a)
b = last_friday_2(datetime.date(2019, 12, 5))
print(b)
