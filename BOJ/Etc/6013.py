n = int(input())
c = []
for _ in range(n):
    x, y = map(int, input().split())
    c.append((x, y))

m = 0
a, b = 0, 0
for i in range(n):
    for j in range(i+1, n):
        d = (c[i][0] - c[j][0])**2 + (c[i][1] - c[j][1])**2
        if d > m:
            m = d
            a, b = i+1, j+1

print(a, b)
