# Solved on 2022. 2. 12.
# 15486 퇴사 2

import sys
input = sys.stdin.readline

N = int(input())
table = [0] * (N+1)
for i in range(1, N+1):
    t, p = map(int, input().split())
    if i + t - 1 < N+1:
        table[i+t-1] = max(table[i+t-1], table[i-1]+p)
    table[i] = max(table[i], table[i-1])
print(table[-1])
