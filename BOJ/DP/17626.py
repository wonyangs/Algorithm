# Solved on 2022. 3. 7.
# 17626 Four Squares

import math
import sys
input = sys.stdin.readline

N = int(input())
dp = [int(1e9)] * (N+1)
dp[0] = 0
n = 1
while n**2 <= N:
    dp[n**2] =1
    n+=1

for i in range(2, N+1):
    for j in range(1, math.floor(i ** 0.5)+1):
        dp[i] = min(dp[i], (i // (j**2) + dp[i%(j**2)]))

print(dp[-1])
