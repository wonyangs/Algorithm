import sys

d = sys.stdin.read().split()
if d:
    for i in range(1, int(d[0]) * 2, 2):
        print((min(int(d[i]), int(d[i+1])) - 1) * 2)
