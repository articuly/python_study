# coding:utf-8
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母函数
def rndchar():
    return chr(random.randint(65, 90))


# 随机颜色1函数
def rndcolor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色2函数
def rndcolor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


# 新建图像
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)

# 创建Draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndcolor())

# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndchar(), fill=rndcolor2(), font=font, )

# 模糊处理
image = image.filter(ImageFilter.BLUR)
image.save('rndcode.jpg', 'jpeg')
