import sys

d = sys.stdin.read().split()
if d:
    n = int(d[0])
    p = 1
    for _ in range(n):
        s = d[p]
        w = int(d[p+1])
        p += 2
        b = ""
        m = 999
        for _ in range(w):
            c = d[p]
            p += 1
            f = sum(x != y for x, y in zip(s, c))
            if f < m:
                m = f
                b = c
        print(b)
