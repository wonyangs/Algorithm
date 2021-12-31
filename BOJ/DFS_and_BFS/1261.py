# Solved on 2021. 09. 14.
# 1261 알고스팟

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

graph = []
visited = [[-1] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().strip())))


def bfs(x, y, graph, visited):
    queue = deque()
    queue.append([x, y])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    queue.appendleft([nx, ny])
                    visited[nx][ny] = visited[x][y]
                if graph[nx][ny] == 1:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1


bfs(0, 0, graph, visited)
print(visited[n-1][m-1])
