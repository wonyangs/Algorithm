# Solved on 2021. 09. 01.
# 11722 가장 긴 감소하는 부분 수열

import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
dp = [1] * N

for i in range(N-1, -1, -1):
    for j in range(i, N):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
