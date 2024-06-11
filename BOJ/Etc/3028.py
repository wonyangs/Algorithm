s = input()

b = 1
for c in s:
    if c == 'A':
        if b == 1:
            b = 2
        elif b == 2:
            b = 1
    elif c == 'B':
        if b == 2:
            b = 3
        elif b == 3:
            b = 2
    else:
        if b == 1:
            b = 3
        elif b == 3:
            b = 1
print(b)
