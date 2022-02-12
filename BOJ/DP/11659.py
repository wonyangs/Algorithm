# Solved on 2022. 2. 12.
# 11659 구간 합 구하기 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [*map(int, input().split())]
prefix = [0]
for n in arr:
    prefix.append(prefix[-1]+n)
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j]-prefix[i-1])
