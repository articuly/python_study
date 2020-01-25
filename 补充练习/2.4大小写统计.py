s = 'Hello world!'
u, l = 0, 0
for e in s:
    if e.isupper():
        u += 1
    if e.islower():
        l += 1

print(f'UPPER CASE {u}')
print(f'LOWER CASE {l}')
