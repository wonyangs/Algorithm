# Solved on 2021. 08. 31.
# 11057 오르막 수

import sys
input = sys.stdin.readline

N = int(input())

d = [1] * 10
tmp = [0] * 10

for i in range(N-1):
    for j in range(10):
        tmp[j] = sum(d[j:])
    d = tmp.copy()

print(sum(d) % 10007)
