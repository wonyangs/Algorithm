# Solved on 2022. 2. 27.
# 2096 내려가기

import sys
input = sys.stdin.readline

N = int(input())
dp = [*map(int, input().split())]
mdp = dp[:]
for n in range(1, N):
    arr = [*map(int, input().split())]
    min_arr, max_arr = [], []
    min_arr.append(arr[0] + min(mdp[0], mdp[1]))
    min_arr.append(arr[1] + min(mdp[0], mdp[1], mdp[2]))
    min_arr.append(arr[2] + min(mdp[1], mdp[2]))
    max_arr.append(arr[0] + max(dp[0], dp[1]))
    max_arr.append(arr[1] + max(dp[0], dp[1], dp[2]))
    max_arr.append(arr[2] + max(dp[1], dp[2]))
    dp, mdp = max_arr, min_arr

print(max(dp), min(mdp))
