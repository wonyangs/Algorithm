# Solved on 2021. 09. 01.
# 13398 연속합 2

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [[-1e9] * 2 for _ in range(n)]
dp[0][0] = A[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0]+A[i], A[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1]+A[i])

maxNum = -1e9

for i in range(2):
    for j in range(n):
        maxNum = max(maxNum, dp[j][i])

print(maxNum)
