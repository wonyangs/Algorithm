import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0] * M for _ in range(N)]
arr = [[*map(int, input().split())] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0:
            dp[i][j] = arr[i][j]
        else:
            dp[i][j] = arr[i][j] + min([dp[i-1][k] for k in range(M) if k != j])

print(min(dp[-1]))
