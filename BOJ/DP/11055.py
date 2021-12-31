# Solved on 2021. 09. 01.
# 11055 가장 큰 증가 부분 수열

import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
dp = [0] * N

for i in range(N-1, -1, -1):
    for j in range(i, N):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j]+A[i])
    if dp[i] == 0:
        dp[i] = A[i]

print(max(dp))
