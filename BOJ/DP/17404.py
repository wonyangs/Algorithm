# Solved on 2021. 12. 08.
# 17404 RGB거리 2

import sys
input = sys.stdin.readline


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
INF = int(10e9)

MIN = []
for k in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][k] = graph[0][k]
    for i in range(1, N):
        dp[i][0] = graph[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = graph[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = graph[i][2] + min(dp[i-1][0], dp[i-1][1])
    m = INF
    for i in range(3):
        if i != k and m > dp[N-1][i]:
            m = dp[N-1][i]
    MIN.append(m)
print(min(MIN))
