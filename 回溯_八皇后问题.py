# coding:utf-8
# 判断新旧旗子是否有冲突
def is_conflict(solution, newpos):
    for pos in solution:
        if pos[0] == newpos[0] or pos[1] == newpos[1] or abs(pos[0] - newpos[0]) == abs(pos[1] - newpos[1]):
            return True
    return False


def play(row=0, solution=[]):
    checker = 8
    # 从第一行开始
    if row == checker:
        yield solution
    else:
        for i in range(checker):
            newpos = (row + 1, i)  # 用新位置探索是否符合规则
            if not is_conflict(solution, newpos):
                for sol in play(row + 1, solution + [newpos]):  # 加入结果，回到开始处再探索
                    yield sol  # 探索完毕后，返回所有结果到生成器


c = 0
for i in play():
    c += 1
    print(i)
    for chess in i:
        index=chess[1]
        print('○'*index,'※','○'*(7-index),sep='')
    print('~'*30)
print(c)

