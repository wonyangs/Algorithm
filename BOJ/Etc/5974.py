import sys

d = sys.stdin.read().split()
c, n = int(d[1]), int(d[2])
for i in range(c):
    s, p = int(d[3+i*2]), int(d[4+i*2])
    print(abs(p - n) + s)
