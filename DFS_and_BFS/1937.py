# Solved on 2021. 11. 18.
# 1937 욕심쟁이 판다

import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline


def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] > graph[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

res = 0
for i in range(N):
    for j in range(N):
        res = max(res, dfs(i, j))
print(res)
