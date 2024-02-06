import sys

input = sys.stdin.readline

N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]

dp = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][i] = 0

for k in range(1, N):
    for i in range(N - k):
        for j in range(i, i + k):
            dp[i][i + k] = min(dp[i][i + k], dp[i][j] + dp[j + 1][i + k] + mat[i][0] * mat[j][1] * mat[i + k][1])

print(dp[0][N-1])
