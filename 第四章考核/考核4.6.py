# coding:utf-8
'''
用A, B, C...G代表图中各点，或用索引号0-6代表图中各点
则示意图为：
    A0
B1       C2
    D3
E4       F5
    G6
接着用接领矩阵表示各点距离：
	A0	B1	C2	D3	E4	F5	G6	x轴
A0	N	1	1.2	N	N	N	N
B1	1	N	N	0.5	2	N	N
C2	1.2	N	N	0.3	N	2	N
D3	N	0.5	0.3	N	1.3	1.5	2.5
E4	N	2	N	1.3	N	N	1
F5	N	N	2	1.5	N	N	0.9
G6	N	N	N	2.5	1	0.9	N
y轴
'''
map = [[None, 1, 1.2, None, None, None, None],
       [1, None, None, 0.5, 2, None, None],
       [1.2, None, None, 0.3, None, 2, None],
       [None, 0.5, 0.3, None, 1.3, 1.5, 2.5],
       [None, 2, None, 1.3, None, None, 1],
       [None, None, 2, 1.5, None, None, 0.9],
       [None, None, None, 2.5, 1, 0.9, None]]


def go_to_end(solution=[], y=0, ):
    if y == 6:  # 现在的点为y，当y到达终点则结束
        yield solution  # 到达终点后返回路经
    else:
        for x in range(y, 7):
            if map[y][x] is None:  # 如果是不可通行的路经则跳过
                continue
            else:
                new_point = (y, x)
                for sol in go_to_end(solution + [new_point], y=x):  # 走到新的点后，现在的点y为新的点
                    yield sol


count = 0
lst = []
for i in go_to_end():
    count += 1
    distance = 0
    for point in i:
        distance += map[point[0]][point[1]]
    lst.append(distance)
    print('路经：{0}，全长距离：{1:0.1f}'.format(i, distance))
print('共有{0}种走法'.format(count))
print('出发点到终点最短的距离为{0}'.format(min(lst)))
