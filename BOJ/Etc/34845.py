import sys

n, x = map(int, sys.stdin.readline().split())
s = sum(map(int, sys.stdin.readline().split()))

v = x * n - s
d = 100 - x

if v <= 0:
    print(0)
else:
    print((v + d - 1) // d)
