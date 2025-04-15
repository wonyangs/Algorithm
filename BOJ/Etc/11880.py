import sys

input = sys.stdin.read
d = input().split()

t = int(d[0])
i = 1

for _ in range(t):
    a = int(d[i])
    b = int(d[i+1])
    c = int(d[i+2])
    i += 3
    r1 = (a + b) ** 2 + c ** 2
    r2 = (a + c) ** 2 + b ** 2
    r3 = (b + c) ** 2 + a ** 2
    print(min(r1, r2, r3))
