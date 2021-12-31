# Solved on 2021. 11. 19.
# 2468 안전 영역

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)


def dfs(x, y, r):
    visit[x][y] = count

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] > r and visit[nx][ny] == 0:
                dfs(nx, ny, r)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
MAX = -1
for i in range(N):
    MAX = max(MAX, max(graph[i]))

res = -1
for n in range(0, MAX+1):
    visit = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > n and visit[i][j] == 0:
                count += 1
                dfs(i, j, n)
    res = max(count, res)

print(res)
