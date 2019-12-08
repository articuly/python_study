# coding:utf-8
import calendar as ca
import time
import re


# 指定日期分为三个参数传入函数
def func(year, month, day):
    ds = ca.monthrange(year, month)[1]
    last_day = (year, month, ds)
    print('该日期当月最后一天是{0}年{1}月{2}日,该月有{3}天。'.format(last_day[0], last_day[1], last_day[2], ds))
    return last_day, ds


a = func(2019, 12, 6)
print(a)


# 指定日期以文本形式传入函数
# 日期格式来源：https://zh.wikipedia.org/wiki/各地日期和时间表示法
def is_a_day(someday):
    # 用正则表达式匹配标准的日期格式
    result = re.match(r'^(\d{1,4})\D+(\d{1,2})\D+(\d{1,4})$', someday)
    the_day = '{0}-{1}-{2}'.format(result.group(1), result.group(2), result.group(3))
    # 尝试将不同日期格式转为结构化时间格式
    try:
        a_day = time.strptime(the_day, '%Y-%m-%d')
    except ValueError:
        try:
            a_day = time.strptime(the_day, '%d-%m-%Y')
        except ValueError:
            try:
                a_day = time.strptime(the_day, '%m-%d-%Y')
            except ValueError:
                print('指定的日期格式不正确。')
    print(a_day)
    # 计算最后一天的日期和该月天数
    ds = ca.monthrange(a_day[0], a_day[1])[1]
    last_day = (a_day[0], a_day[1], ds)
    print('该日期当月最后一天是{0}年{1}月{2}日,该月有{3}天。'.format(last_day[0], last_day[1], last_day[2], ds))
    return last_day, ds


b=is_a_day('11/11/2021')
print(b)
