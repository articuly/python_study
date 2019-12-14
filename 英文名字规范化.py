# coding:utf-8
L1 = ['adam', 'LISA', 'barT']
def normalize(name):
    return name.title()
L2 = list(map(normalize, L1))
print(L2)

