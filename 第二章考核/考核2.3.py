# coding:utf-8
class Quote:
    quotes = {'子日': '学而时习之，不亦说乎。', '李白': '安能摧眉折腰事权贵，使我不得开心颜。',
              '老子': '上善若水，水利万物而不争。', '苏轼': '明月几时有，把酒问青天。'}

    def __init__(self, name):
        if name == '孔子':
            self.name = '子日'
        else:
            self.name = name
        self.word = Quote.quotes.get(self.name)

    def __str__(self):
        return '{0}：{1}'.format(self.name, self.word)

    __repr__ = __str__


a = Quote('李白')
print(a)
b = Quote('孔子')
print(b)
c = Quote('杜甫')
print(c)
d = Quote('苏轼')
print(d)
