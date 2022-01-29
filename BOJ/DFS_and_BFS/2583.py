# Solved on 2022. 1. 29.
# 2583 영역 구하기

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    count = 2
    graph[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = count
                count += 1
                queue.append((nx, ny))
    return count - 1


M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
for _ in range(K):
    ax, ay, bx, by = map(int, input().split())
    for i in range(ay, by):
        for j in range(ax, bx):
            graph[i][j] = -1

res = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            res.append(bfs(i, j))

res.sort()
print(len(res))
print(*res)
