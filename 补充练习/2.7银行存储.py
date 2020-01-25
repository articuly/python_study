acc = 0
while True:
    x = input('please deal with your account:')
    if x == 'q':
        break
    else:
        y = x.split(' ')
        if y[0] in ('D', 'd'):
            acc += float(y[1])
        elif y[0] in ('W', 'w'):
            acc -= float(y[1])
            if acc < 0:
                print('can not deal with it, you withdraw too much money, because your account has not enough money')
                acc += float(y[1])
        else:
            raise Exception('please enter your dealing')
        print(f'your account is {acc:.2f} yuan')
