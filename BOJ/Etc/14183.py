import sys

d = sys.stdin.read().split()
i = 0
while i < len(d):
    m = int(d[i])
    n = int(d[i+1])
    i += 2
    if m == 0 and n == 0:
        break
    t = [int(x) for x in d[i:i+m]]
    i += m
    c = 0
    for _ in range(n):
        k = [int(x) for x in d[i:i+m]]
        i += m
        if all(k[j] <= t[j] for j in range(m)):
            c += 1
    print(c)
