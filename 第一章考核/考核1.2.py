# coding:utf-8
score = [9.9, 9.2, 8.1, 9.7, 10, 8.3, 8.6, 9.5, 8.4]
# 去掉最高分和最低分
score.remove(max(score))
score.remove(min(score))
# 计算最终得分，保留一位小数
s = round(sum(score) / len(score), 1)
print('歌手的最终得分是{0}'.format(s))

# 补充方法
score.sort()
min, *sco, max = score
avg = round(sum(sco) / len(sco), 1)
print(avg)
