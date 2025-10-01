n = int(input())
sx, sy, ex, ey = map(int, input().split())
m = float('inf')
r = 0
for i in range(1, n+1):
    k = int(input())
    p = [(sx, sy)] + [tuple(map(int, input().split())) for _ in range(k)] + [(ex, ey)]
    d = sum(abs(p[j][0]-p[j+1][0]) + abs(p[j][1]-p[j+1][1]) for j in range(len(p)-1))
    if d < m:
        m = d
        r = i
print(r)
