# coding:utf-8
# import pprint
# import requests
#
# api = 'https://api.github.com/users/articuly'
# q = requests.get(api)
# print(q)
# pprint.pprint(q.json())
# 百度语音合成示例
from aip import AipSpeech
import re

APP_ID = '17954919'
API_KEY = '2r2vNoOhRr4Zz7ompa0azdrc'
SECRET_KEY = 'eSnGTZlFBBzlQuxrQCiBbl5i2y5qjzyo'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
s = input("请输入要合成语音的文字（直接回车将工作目录下tts.txt文件转换成语音）：")

if 0<len(s) < 1024:
    sv = [s]
    print(sv)
elif len(s)==0:
    with open('./tts.txt') as f:
        sv=[f.read()]
        print(sv)
else:
    sv = re.findall(r'.{1024}', s)
    print(sv)
count = 1
for i in sv:
    sound = client.synthesis(i, 'zh', 1, {'vol': 5, 'per': 4, 'spd': 4, 'pit': 5})
    if not isinstance(sound, dict):
        with open('./tts{0}.mp3'.format(count), 'wb') as svf:
            svf.write(sound)
            print('tts{0}.mp3 is OK'.format(count))
            count += 1
    else:
        print('something is wrong')
