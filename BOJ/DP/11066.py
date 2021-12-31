# Solved on 2021. 12. 18.
# 11066 파일 합치기

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    prefix = [0] * (N+1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + arr[i-1]

    dp = [[0] * N for _ in range(N)]
    for i in range(2, N+1):
        for j in range(N+1-i):
            dp[j][j+i-1] = min(dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)) + (prefix[j+i] - prefix[j])
    print(dp[0][-1])
