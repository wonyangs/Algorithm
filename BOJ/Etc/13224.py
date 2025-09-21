s = input()
p = 1
for m in s:
    if m == 'A':
        if p == 1:
            p = 2
        elif p == 2:
            p = 1
    elif m == 'B':
        if p == 2:
            p = 3
        elif p == 3:
            p = 2
    else:
        if p == 1:
            p = 3
        elif p == 3:
            p = 1
print(p)
