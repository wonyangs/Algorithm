s = {'a', 'e', 'i', 'o', 'u'}

a, b = 0, 0
for c in input():
    if c in s:
        a += 1
        b += 1
    if c == 'y':
        b += 1
print(a, b)
