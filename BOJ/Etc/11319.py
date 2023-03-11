m = 'aeiouAEIOU'
for _ in range(int(input())):
    a, b = 0, 0
    for c in input():
        if c == ' ':
            continue
        if c in m:
            b += 1
        else:
            a += 1
    print(a, b)
