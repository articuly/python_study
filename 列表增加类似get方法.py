# coding:utf-8
def get_index(lst,i,default=None):
    try:
        return lst[i]
    except IndexError:
        return default
lst=list(range(-5,5))
g=get_index
print(g(lst,5))
print(g(lst,12))