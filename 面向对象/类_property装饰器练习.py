# coding:utf-8
# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen:
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        self._height = h

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1920*2
s.height = 1080*2
print('resolution =', s.resolution)
if s.resolution == 8294400:
    print('测试通过!')
else:
    print('测试失败!')
