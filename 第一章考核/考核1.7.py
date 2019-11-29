# coding:utf-8
# 创建判断后缀是图片格式的函数，图片文件后缀为('.jpg','.gif','.png')
def is_picture(file):
    name = file.split('.')
    if name[-1] in ('jpg', 'gif', 'png'):
        return file


lst = ['a.py', 'b.jpg', 'c.gif', 'd.map', 'e.png', 'f.jpg', 'k.txt', 'f.gif', 'h.png', 'm.docx']
pic_lst1 = filter(is_picture, lst)
print(list(pic_lst1))
pic_lst2 = filter(is_picture, ['h.png', 'm.docx', 'l.py.gif', 'n.gif.doc'])
print(list(pic_lst2))
