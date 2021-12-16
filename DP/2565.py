# Solved on 2021. 12. 16.
# 2565 전깃줄

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
dp = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i][1] > arr[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(N-max(dp))
