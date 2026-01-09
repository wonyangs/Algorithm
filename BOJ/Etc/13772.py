n = int(input())
for _ in range(n):
    s = input()
    k = 0
    for c in s:
        if c in 'ADOPQR':
            k += 1
        elif c == 'B':
            k += 2
    print(k)
