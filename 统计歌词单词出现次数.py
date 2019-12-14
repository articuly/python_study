# coding:utf-8
songs = 'You raise my up so I can stand on mountains You raise my up to walk on stormy seas I am strong when I am on your shoulders You raise me up to more than I can be'
# 制作上述歌词的单词表
songs = songs.lower()
lst = songs.split(' ')
lst = list(set(lst))
print(lst)
# 统计每个单词出现的资料
for n in lst:
    print(n, '出现了', songs.count(n), '次')
