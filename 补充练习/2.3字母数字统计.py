s = 'hello world!123'
l = 0
d = 0
for e in s:
    if e.isalpha():
        l += 1
    if e.isdigit():
        d += 1

print(f'LETTER {l}')
print(f'DIGITS {d}')
