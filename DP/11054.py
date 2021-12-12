# Solved on 2021. 12. 12.
# 11054 가장 긴 바이토닉 부분 수열

import sys
input = sys.stdin.readline

N = int(input())
arrA = list(map(int, input().split()))
arrB = arrA[::-1]

dpA = [1] * N
dpB = [1] * N
for i in range(N):
    for j in range(i):
        if arrA[j] < arrA[i]:
            dpA[i] = max(dpA[i], dpA[j] + 1)
        if arrB[j] < arrB[i]:
            dpB[i] = max(dpB[i], dpB[j] + 1)
dpB.reverse()

dp = [0] * N
for i in range(N):
    dp[i] = dpA[i] + dpB[i] - 1
print(max(dp))
