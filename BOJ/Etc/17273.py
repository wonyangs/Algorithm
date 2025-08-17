import sys

d = list(map(int, sys.stdin.read().split()))
it = iter(d)
n = next(it)
m = next(it)

a = [0] * n
b = [0] * n
v = [0] * n

for i in range(n):
    a[i] = next(it)
    b[i] = next(it)
    v[i] = a[i]

for _ in range(m):
    k = next(it)
    for i in range(n):
        if v[i] <= k:
            v[i] = a[i] + b[i] - v[i]

print(sum(v))
