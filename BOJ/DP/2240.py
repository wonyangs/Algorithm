# Solved on 2022. 2. 12.
# 2240 자두나무

import sys
input = sys.stdin.readline

T, W = map(int, input().split())
dp = [0] * (W+1)
for t in range(1, T+1):
    tree = int(input())
    if tree == 1:
        for i in range(1, W, 2):
            if i > t: continue
            dp[i+1] = max(dp[i+1], dp[i])
        for i in range(0, W+1, 2):
            if i > t: continue
            dp[i] += 1
    else:
        for i in range(0, W, 2):
            if i > t: continue
            dp[i+1] = max(dp[i+1], dp[i])
        for i in range(1, W+1, 2):
            if i > t: continue
            dp[i] += 1
print(max(dp))

