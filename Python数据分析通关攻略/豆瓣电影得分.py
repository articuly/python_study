# coding:utf-8
# 简易demo，爬取豆瓣电影的清单与得分
import json
import re
import requests
from requests import RequestException

# 获取网页的内容，以文本形式返回
def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 对网页文本内容进行解析
def parse_page(html):
    pattern = re.compile('<li.*?list-item.*?data-title="(.*?)".*?data-score="(.*?)".*?>.*?<img.*?src="(.*?)".*?/>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'title': item[0],
            'score': item[1],
            'image': item[2],}

# 爬虫主程序，同时print效果
def main():
    url = "https://movie.douban.com/cinema/nowplaying/beijing/"
    html = get_page(url)
    print(html)
    for item in parse_page(html):
        print(item)

if __name__ == '__main__':
    main()