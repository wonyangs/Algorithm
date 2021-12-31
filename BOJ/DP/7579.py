# Solved on 2021. 12. 07.
# 7579 앱

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memory = list(map(int, input().split()))
coin = list(map(int, input().split()))

maxCoin = sum(coin) + 1
dp = [[0] * maxCoin for _ in range(N)]
for i in range(maxCoin):
    if coin[0] <= i:
        dp[0][i] = memory[0]
for i in range(N):
    for j in range(maxCoin):
        if coin[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(memory[i] + dp[i-1][j - coin[i]], dp[i-1][j])
for i in range(maxCoin):
    if dp[N-1][i] >= M:
        print(i)
        break
