# Solved on 2021. 12. 17.
# 2293 동전 1

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
arr.sort()

dpA = [0] * (K+1)
dpB = [0] * (K+1)
for i in range(1, N+1):
    for j in range(1, K+1):
        dpB[j] = dpA[j]
        if arr[i] == j:
            dpB[j] += 1
        if arr[i] < j:
            dpB[j] += dpB[j-arr[i]]
    dpA = dpB[:]

print(dpB[-1])
