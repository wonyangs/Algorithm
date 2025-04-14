n, q = map(int, input().split())
a = [0]*(n+1)
for _ in range(q):
    L, I = map(int, input().split())
    for x in range(L, n+1, I):
        if a[x] == 0:
            a[x] = 1
r = a.count(0) - 1
print(r)
