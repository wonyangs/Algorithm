import math

n = int(input())
p = []
for _ in range(n):
    x, y = map(float, input().split())
    p.append((x, y))

m = int(input())
for _ in range(m):
    k = int(input())
    r = list(map(int, input().split()))
    d = 0
    for i in range(k-1):
        x1, y1 = p[r[i]]
        x2, y2 = p[r[i+1]]
        d += math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print(round(d))
