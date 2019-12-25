# coding:utf-8
# 打印开始到结束日期的所有日期
from datetime import datetime, timedelta


def date_between(start, end):
    try:
        start_day = datetime.strptime(start, '%Y-%m-%d')
        end_day = datetime.strptime(end, '%Y-%m-%d')
        if end_day - start_day < timedelta(days=1):
            start_day, end_day = end_day, start_day  # 远期日期与近期日期互换，保证远期日期在后
        all_day = []
        while start_day != end_day:
            result = datetime.strftime(start_day, '%Y-%m-%d')
            print(result)
            start_day = start_day + timedelta(days=1)
            all_day.append(result)  # 把所有日期放到一个列表
        print(datetime.strftime(end_day, '%Y-%m-%d'))  # 打印最后一天
        return all_day + [datetime.strftime(end_day, '%Y-%m-%d')]  # 添加最后一天到列表
    except ValueError:
        print("指定的日期格式不正确，请以'XXXX-XX-XX'的格式输入年月日。")


d = date_between('2019-12-25', '2020-1-10')
print('-' * 30)
e = date_between('2020-xx-x', '2014-45-5')
print('-' * 30)
f = date_between('2020-1-15', '2020-1-10')
print(f)
print('-' * 30)
g = date_between('2019-12-25', '2019-12-25')


# 另一种方法
def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)


start_dt = date(2019, 12, 25)
end_dt = date(2020, 1, 10)
for dt in daterange(start_dt, end_dt):
    print(dt.strftime("%Y-%m-%d"))
