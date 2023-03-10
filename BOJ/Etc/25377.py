N = int(input())
res = -1
for _ in range(N):
    a, b = map(int, input().split())
    if a <= b:
        if res == -1:
            res = b
        else:
            res = min(res, b)
print(res)
