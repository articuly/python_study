# coding:utf-8
class Sale:
    total_num = 0
    total_volume = 0
    all_info = {}

    # 初始化销售商品的名称、价格、数量
    def __init__(self, product, price, num):
        self.product = product
        self.price = price
        self.num = num
        self.__discount = 0.9  # 防止修改商品折扣率
        self.__wholesale = 20  # 防止修改商品起批数量
        Sale.total_num += self.num  # 更新已销售商品累计数量
        if self.num < self.__wholesale:  # 判断销售时是否达到起批数量
            self.sub_volume = self.price * self.num
        else:
            self.sub_volume = self.price * self.num * self.__discount
        Sale.total_volume += self.sub_volume  # 更新已销售商品累计金额
        Sale.all_info.update({self.product: (self.num, self.sub_volume)})  # 将已销售商品信息放到一个字典

    # 显示单个商品销售信息
    def sale_info(self):
        print('{0}商品销售了{1}件，销售金额是{2}元。'.format(self.product, self.num, self.sub_volume))

    @classmethod
    def amount(cls):
        print('所有商品销售的总量是{0}件。'.format(Sale.total_num))

    @classmethod
    def volumes(cls):
        print('所有商品销售的总额是{0}元。'.format(Sale.total_volume))

    # 查找某个商品的销售信息
    @classmethod
    def product_info(cls, product):
        if Sale.all_info.get(product):
            print('{0}商品已经卖了{1}件，销售金额为{2}元。'.format(product, Sale.all_info.get(product)[0],
                                                    Sale.all_info.get(product)[1]))
        else:
            print('没有找到您查询商品的销售信息。')


a = Sale('book', 30, 5)
a.sale_info()
b = Sale('meat', 40, 10)
b.sale_info()
c = Sale('apple', 5, 30)
c.sale_info()
Sale.amount()
Sale.volumes()
d = Sale('cake', 10, 30)
d.__discount = 0.5
d.sale_info()
Sale.volumes()
Sale.product_info('book')
Sale.product_info('fruit')


# 建议将类属性改成这种形式，Sale.total_num 换成 cls.total_num
# 参考答案
class Goods:
    def __init__(self, sales_number, price, discount_number=5):
        self.sales_number = sales_number
        self.price = price
        self.discount_number = discount_number
        d = self.sales_number - self.discount_number
        if d >= 0:
            if d <= 11:
                self.discount_percent = 0.9
            else:
                self.discount_percent = 0.8
        else:
            self.discount_percent = 0.99

    def sale_number(self):
        return self.sales_number

    def total(self):
        t = self.sales_number * self.price * self.discount_percent
        return t


apple = Goods(10, 9)
print("number: ", apple.sale_number())
print("total: ", apple.total())
