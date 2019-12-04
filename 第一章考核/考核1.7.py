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


# 补充方法
def any_true(predicate, sequence):
    return True in map(predicate, sequence)


list_dir = ['a.py', 'b.jpg', 'c.gif', 'd.map', 'e.png', 'f.jpg', 'k.txt', 'f.gif', 'h.png', 'm.docx']
pic_ext = ('.jpg', '.gif', '.png')
pics = [img for img in list_dir if any_true(img.endswith, pic_ext)]
print(list_dir)
print(pics)
