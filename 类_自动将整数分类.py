# coding:utf-8
class Diff:
    def __init__(self, *num):
        self.num = num

    def odd_or_even(self):
        odd_list = [i for i in self.num if i % 2 == 1]
        even_list = [i for i in self.num if i % 2 == 0]
        return odd_list, even_list

    def prime_or_composite(self):
        prime_list = [i for i in self.num if Diff.is_prime(i)]
        composite_list = [i for i in self.num if i not in prime_list and i != 1]
        return prime_list, composite_list

    @staticmethod
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True


a = Diff(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a.odd_or_even())
print(a.prime_or_composite())

