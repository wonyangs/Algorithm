import sys

d = sys.stdin.read().split()
if d:
    for i in range(1, len(d), 3):
        n, c, s = int(d[i]), int(d[i+1]), d[i+2]
        for _ in range(c):
            s = s[n:] + s
        print(s)
