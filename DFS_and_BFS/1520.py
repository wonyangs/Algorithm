# Solved on 2021. 11. 19.
# 1520 내리막 길

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    tmp = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] < graph[x][y]:
                tmp += dfs(nx, ny)
    dp[x][y] = tmp
    return dp[x][y]


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dp[M-1][N-1] = 1
print(dfs(0, 0))
