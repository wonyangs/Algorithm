n = int(input())
s0, c0, l0 = map(int, input().split())
best = (-s0, c0, l0)
res = 1
for i in range(2, n + 1):
    s, c, l = map(int, input().split())
    cur = (-s, c, l)
    if cur < best:
        best = cur
        res = i
print(res)
