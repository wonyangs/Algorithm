# Solved on 2022. 2. 12.
# 2748 피보나치 수 2

import sys
input = sys.stdin.readline

n = int(input())
a, b = 0, 1
if n == 1:
    print(b)
else:
    for _ in range(2, n+1):
        tmp = a + b
        a = b
        b = tmp
    print(tmp)
