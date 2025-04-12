n = int(input())
m = int(input())
a = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(m)]
res = [0] * n

for i in range(m):
    t = a[i] - 1
    b = s[i]
    miss = 0
    for j in range(n):
        if j == t:
            res[j] += 1
        elif b[j] - 1 == t:
            res[j] += 1
        else:
            miss += 1
    res[t] += miss

for r in res:
    print(r)
