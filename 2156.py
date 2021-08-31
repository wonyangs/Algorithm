# Solved on 2021. 09. 01.
# 2156 포도주 시식

import sys
input = sys.stdin.readline

N = int(input())

g = [0] * 10001
dp = [0] * 10001

for i in range(1, N+1):
    g[i] = int(input())

dp[1] = g[1]
dp[2] = g[1] + g[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-1], g[i-1]+dp[i-3]+g[i], dp[i-2]+g[i])

print(dp[N])
