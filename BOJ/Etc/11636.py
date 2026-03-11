import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a = list(map(int, sys.stdin.readline().split()))
    s = 0
    for i in range(1, len(a) - 1):
        if a[i] > a[i-1] * 2:
            s += a[i] - a[i-1] * 2
    print(s)
