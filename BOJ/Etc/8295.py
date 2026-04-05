import sys

n, m, p = map(int, sys.stdin.read().split())
a = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if 2 * (i + j) >= p:
            a += (n - i + 1) * (m - j + 1)

print(a)
