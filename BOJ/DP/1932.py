# Solved on 2021. 09. 15.
# 1932 정수 삼각형

import sys
input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

dp = [[0] * (i+3) for i in range(n)]
dp[0][1] = array[0][0]

for i in range(1, n):
    for j in range(1, i+2):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j-1]

print(max(dp[n-1]))
