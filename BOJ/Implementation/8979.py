N, K = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
x, y, z = 0, 0, 0
for a, b, c, d in arr:
    if a == K:
        x, y, z = b, c, d
cnt = 0
for a, b, c, d in arr:
    if b > x:
        cnt += 1
    elif b == x and c > y:
        cnt += 1
    elif b == x and c == y and d > z:
        cnt += 1
print(cnt + 1)
