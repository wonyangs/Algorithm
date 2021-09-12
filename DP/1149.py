# Solved on 2021. 09. 12.
# 1149 RGB거리

import sys
input = sys.stdin.readline

n = int(input())
price = [[0, 0, 0]]
dp = [[0] * 3 for _ in range(n+1)]

for _ in range(n):
    price.append(list(map(int, input().split())))

dp[1][0] = price[1][0]
dp[1][1] = price[1][1]
dp[1][2] = price[1][2]

for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + price[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + price[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + price[i][2]

print(min(dp[n]))
