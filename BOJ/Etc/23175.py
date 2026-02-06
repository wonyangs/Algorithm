import sys
d = list(map(int, sys.stdin.read().split()))
n = d[0]
a = d[1:]
r = []
i = 0
while i < n:
    v = a[i]
    r.append(v)
    i += v
print(*r)
