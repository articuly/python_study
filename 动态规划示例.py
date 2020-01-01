# coding:utf-8
# 物品列表
# 第一个物品为空，方便从0开始遍历
items = {0: (0, 0, None),
         1: (100, 1000, 'pencil'),
         2: (200, 3000, 'mobile'),
         3: (300, 7000, 'ipad'),
         4: (400, 6000, 'vbox'),
         5: (500, 11000, 'macbook')}
# 价值列表
v = {}
# 方案列表
solution = {0: {0: None, 1: 2}, }
# 负责步长，取所有物品的最大公约数，这样可以计算最小剩余空间的价值
step = 100
for i in range(0, len(items)):  # 遍历不同物品阶段
    v[i] = {}
    solution[i] = {}
    for j in range(0, 500 + step, step):  # 遍历可容纳量
        v[i][j] = 0
        solution[i][j] = []
        print(solution[i])
        print('-' * 50)
        if i == 0:  # 物品为空状态
            continue
        if j < items[i][0]:  # 放不下
            v[i][j] = v[i - 1][j]
        else:  # 放得下，取这一次价值与之前同等负重的价值的最大值
            #  上一阶段的最大价值比这阶段物品价值加剩余空间最大大价值的大
            if v[i - 1][j] > items[i][1] + v[i - 1][j - items[i][0]]:  # 核心判断
                v[i][j] = v[i - 1][j]
                solution[i][j] = solution[i - 1][j]
            #  新物品价值加可用空间最大价值更大
            else:
                v[i][j] = items[i][1] + v[i - 1][j - items[i][0]]
                solution[i][j] = solution[i - 1][j - items[i][0]] + [i]
        print(solution[i])
        print('/'*50)
print(v[i][j])
print(solution)
