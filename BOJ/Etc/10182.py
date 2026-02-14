import math

n = int(input())
for _ in range(n):
    d = input().split()
    v = float(d[2])
    if d[0] == 'H':
        res = -math.log10(v)
    else:
        res = 14 + math.log10(v)
    print(f"{res:.2f}")
