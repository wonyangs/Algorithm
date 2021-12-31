# Solved on 2021. 09. 01.
# 9465 스티커

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    dp = [[0] * 2 for _ in range(n+1)]
    tmp = []

    for i in range(2):
        tmp = list(map(int, input().split()))
        for j in range(1, n+1):
            dp[j][i] = tmp[j-1]

    dp[1][0] += dp[0][1]
    dp[1][1] += dp[0][0]

    for i in range(2, n+1):
        dp[i][0] += max(dp[i-2][1], dp[i-1][1])
        dp[i][1] += max(dp[i-2][0], dp[i-1][0])

    maxNum = 0
    for i in range(1, n+1):
        for j in range(2):
            if maxNum < dp[i][j]:
                maxNum = dp[i][j]

    print(maxNum)
