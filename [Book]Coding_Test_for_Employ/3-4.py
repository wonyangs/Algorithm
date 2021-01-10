# Solved on 2020.12.28
# 3-4 1이 될 때까지

# ---------------------------

import sys
input = sys.stdin.readline

count = 0

n, k = map(int, input().split())

while n > 1:
    count += n - (k * (n//k))
    n = k * (n//k)

    n /= k
    count += 1

print(int(count))
