# coding:utf-8
import logging
from functools import wraps


# 简单装饰器
def simple_deco(func):
    def wrapper(*args):
        print('func is', func)
        print('args is', args)
        logging.warning("{0} is running".format(func.__name__))
        return func(*args)

    return wrapper


@simple_deco
def foo():
    print('i am foo.')
    return


@simple_deco
def mysum(*args):
    return sum(args)


foo()
print(mysum(1, 2, 3))


# 带参数的装饰器
def more_deco(level='warn'):
    def decorator(func):
        def wrapper(*args):
            print('func is', func)
            print('args is', args)
            if level == 'warn':
                logging.warning("{0} is running.".format(func.__name__))
            else:
                logging.error('{0} is normal.'.format(func.__name__))
            return func(*args)

        return wrapper

    return decorator


@more_deco()
def bar():
    print('i am bar.')


@more_deco(level='abc')
def mymax(*args):
    return max(args)


bar()
print(mymax(4, 7, 12))


# 类装饰器
class Class_deco:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args):
        print('calling class decorator.')
        print('end of classing class decorator.')
        return self._func(*args)  # 返回结果


@Class_deco
def far():
    print('i am far.')


@Class_deco
def mymin(*args):
    return min(args)


far()
print(mymin(9, 8, 4))


# 保留原函数的信息
def logged(func):
    @wraps(func)
    def wrapper(*args):
        print('func is', func)
        print('args is', args)
        print(func.__name__)
        print(func.__doc__)
        return func(*args)

    return wrapper


@logged
def myway(x, y):
    """do some math\ntest for my way"""
    return x ** 2 + 5 * y


print(myway(4, 3))
