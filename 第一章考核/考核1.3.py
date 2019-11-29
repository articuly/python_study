# coding:utf-8
d = {'huawei': 91.2, 'alibaba': 94.1, 'qq': 90.1, 'baidu': 89.4, 'xiaomi': 88.4}
for k, v in d.items():
    if v == min(d.values()):
        print("字典中值最小的键值对是'{0}':{1}".format(k, v))
