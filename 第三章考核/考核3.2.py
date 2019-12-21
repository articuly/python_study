# coding:utf-8
from datetime import datetime, timedelta


def date_between(start, end):
    try:
        start_day = datetime.strptime(start, '%Y-%m-%d')
        end_day = datetime.strptime(end, '%Y-%m-%d')
        if end_day - start_day < timedelta(days=1):
            start_day, end_day = end_day, start_day
        all_day = []
        while start_day != end_day:
            result = datetime.strftime(start_day, '%Y-%m-%d')
            print(result)
            start_day = start_day + timedelta(days=1)
            all_day.append(result)
        print(datetime.strftime(end_day, '%Y-%m-%d'))
        return all_day + [datetime.strftime(end_day, '%Y-%m-%d')]
    except ValueError:
        print("指定的日期格式不正确，请以'XXXX-XX-XX'的格式输入年月日。")


d = date_between('2019-12-25', '2020-1-10')
print('-'*30)
e = date_between('2020-xx-x', '2014-45-5')
print('-'*30)
f = date_between('2020-1-25', '2020-1-10')
print('-'*30)
g = date_between('2019-12-25', '2019-12-25')
