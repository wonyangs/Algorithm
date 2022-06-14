# Solved on 2022. 6. 13.
# 2775 부녀회장이 될테야

import sys
input = sys.stdin.readline

T = int(input())

dp = [[i for i in range(15)]]
for _ in range(14):
    dp.append([0] * 15)
for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = sum(dp[i - 1][:j+1])

for _ in range(T):
    a = int(input())
    b = int(input())
    print(dp[a][b])
