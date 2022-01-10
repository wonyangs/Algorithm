# Solved on 2022. 1. 10.
# 2133 타일 채우기

import sys
input = sys.stdin.readline

N = int(input())

if N % 2 == 1:
    print(0)
else:
    dp = [0] * (N+1)
    if N > 1:
        dp[2] = 3
    if N > 3:
        dp[4] = 11
    
    for i in range(6, N+1, 2):
        dp[i] = dp[2] * dp[i-2] + 2
        for j in range(4, i, 2):
            dp[i] += dp[i-j] * 2
    print(dp[N])
    
