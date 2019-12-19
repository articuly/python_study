def fact(n):
    try:
        # 计算正整数的阶乘
        start = n
        result = 1
        while n > 1:
            result = result * n
            n -= 1
        print('{0}! = {1}'.format(start, result))
        # 把结果每个数位的数字累加
        word, end = '', 0
        for i in str(result):
            word = word + ' + ' + i
            end = end + int(i)
        print(word[3:] + ' = ' + str(end))
        return end
    except TypeError:
        return '函数参数必须是正整数。'


a = fact(10)
print(a)
b = fact('abc')
print(b)
c = fact(20)
