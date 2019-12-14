# coding:utf-8
def strong_deco(f):
    def wrapper(name1):
        print('f is', f)
        print('name1 is', name1)
        return '<strong>{0}</strong>'.format(f(name1))
    print('wrapper is', wrapper)
    return wrapper


@strong_deco
def book(name):
    print('name is', name)
    return name


b = book("learn python")
print(b)
