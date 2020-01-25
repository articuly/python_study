n1 = input('please enter some bin number:')
n2 = n1.split(',')
for e in n2:
    if int(e, 2) % 5 == 0:
        print(e, sep=',')

n3 = '0100,0011,1010,1001'
n4 = '1111100,1110101,0000111010,01111,000111001,010101,110011'
