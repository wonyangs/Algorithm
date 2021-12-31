# Solved on 2021. 09. 25.
# 12865 평범한 배낭

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

article = []
dp = [0] * (K+1)

for _ in range(N):
    w, v = map(int, input().split())
    tmp = [0] * (K+1)
    for i in range(K+1):
        if i-w < 0:
            tmp[i] = dp[i]
        else:
            tmp[i] = max(dp[i], dp[i-w] + v)
    for i in range(K+1):
        dp[i] = tmp[i]
print(dp[K])
