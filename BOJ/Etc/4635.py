import sys

d = sys.stdin.read().split()
i = 0
while i < len(d):
    n = int(d[i])
    i += 1
    if n == -1:
        break
    a = 0
    p = 0
    for _ in range(n):
        s = int(d[i])
        t = int(d[i+1])
        i += 2
        a += s * (t - p)
        p = t
    print(f"{a} miles")
