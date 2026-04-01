import sys

a = sys.stdin.read().split()
if a:
    for i in range(int(a[0])):
        p, t, m = int(a[i*3+1]), int(a[i*3+2]), int(a[i*3+3])
        r = 9000 - 15 * p - 20 * t - 25 * m
        f = max(0, (r + 39) // 40)
        print("impossible" if f > 100 else f)
