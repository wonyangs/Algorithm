import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[*map(int, input().split())] for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = arr[0][0]

for i in range(1, M):
    dp[0][i] = dp[0][i-1] + arr[0][i]
for i in range(1, N):
    for j in range(M):
        if j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
            continue
        dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + arr[i][j]

print(dp[-1][-1])
