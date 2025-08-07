import sys
r = sys.stdin.readline
t = lambda a, b, c: a * 3600 + b * 60 + c
x = t(*map(int, r().split()))
for _ in range(int(r())):
    a, *b = map(int, r().split())
    if a < 3:
        x = (x + b[0] * (1 if a == 1 else -1)) % 86400
    else:
        print(x // 3600, x % 3600 // 60, x % 60)
