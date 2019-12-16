from PIL import Image
im=Image.open('articuly.jpg')
w,h=im.size
print(w,h)
im.thumbnail((w//2,h//2))
print('Resize:{0}, {1}'.format(w//2,h//2))
im.save('smallarticuly.jpg','jpeg')