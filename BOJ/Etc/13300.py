n, k = map(int, input().split())
c = [[0] * 2 for _ in range(6)]
for _ in range(n):
    s, y = map(int, input().split())
    c[y-1][s] += 1
r = 0
for y in range(6):
    for s in range(2):
        r += c[y][s] // k + (1 if c[y][s] % k > 0 else 0)
print(r)
