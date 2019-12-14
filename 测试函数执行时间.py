# coding:utf-8
def run_time(func):
    def wrapper():
        import time
        a = time.time()
        print('func is',func)
        func()
        b = time.time()
        return b - a
    print('wrapper is',wrapper)
    return wrapper
def run_times(func):
    import time
    a = time.time()
    print('func is', func)
    func()
    b = time.time()
    return b - a
@run_time
def biglist():
    lst = []
    for i in range(0, 100000):
        lst.append(i)
@run_time
def comprelist():
    [i for i in range(0,100000)]

print(biglist)
print(biglist())
print(comprelist)
print(comprelist())

