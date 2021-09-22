# Solved on 2021. 09. 23.
# 9251 LCS

import sys
input = sys.stdin.readline

stringA = ' ' + input().rstrip()
stringB = ' ' + input().rstrip()

dp = [[0] * len(stringB) for _ in range(len(stringA))]

for i in range(1, len(stringA)):
    for j in range(1, len(stringB)):
        if stringA[i] == stringB[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(stringA)-1][len(stringB)-1])
