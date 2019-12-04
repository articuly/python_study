# coding:utf-8
# 定义类为买书的行为，买一本书为一个实例
class Shopping:
    sub_cost = 0
    total_cost = 0

    def __init__(self, book_name, price, num):
        self.book_name = book_name
        self.price = price
        self.num = num
        Shopping.sub_cost += self.price * self.num

    def info(self):
        print('你买了{0}本{1}，每本书的价格是{2}元。'.format(self.num, self.book_name, self.price))

    @classmethod
    def check(cls):
        if 0 < Shopping.sub_cost < 99:
            print('目前合计书款是{0}元，运费是5元，亲，买满99元包邮哦。'.format(Shopping.sub_cost))
        elif Shopping.sub_cost == 0:
            print('目前亲的购物车是空的，看看有什么喜欢的书。')
        else:
            print('亲，已买了{0}元的书，已满99元，帮你免去邮费了。'.format(Shopping.sub_cost))

    @classmethod
    def checkout(cls):
        if 0 < Shopping.sub_cost < 99:
            total_cost = Shopping.sub_cost + 5
            print('亲，总共书款加运费共{0}元，请完成支付。\n(支付中...)\n祝您购物愉快^_^'.format(total_cost))
            Shopping.sub_cost, Shopping.total_cost = 0, 0
        elif Shopping.sub_cost == 0:
            print('亲，欢迎下次光临，希望会有亲喜欢的书。\n(离开...)')
        else:
            total_cost = Shopping.sub_cost
            print('亲，总共书款为{0}元，请完成支付。\n(支付中...)\n祝您购物愉快^_^'.format(total_cost))
            Shopping.sub_cost, Shopping.total_cost = 0, 0


# 第一次买书
a = Shopping('Python', 30, 1)
b = Shopping('Math', 20, 2)
a.info()
b.info()
Shopping.check()
c = Shopping('AI', 35, 1)
Shopping.check()
Shopping.checkout()
print('------------')
# 第二次买书
d = Shopping('Python', 30, 1)
f = Shopping('Math', 20, 1)
Shopping.check()
Shopping.checkout()
print('------------')
# 第三次，逛了一圈，没买书就离开了
Shopping.check()
Shopping.checkout()
