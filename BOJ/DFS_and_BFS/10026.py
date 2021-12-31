# Solved on 2021. 10. 14.
# 10026 적록색약

from collections import deque
import sys
input = sys.stdin.readline


def sbfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1
    color = graph[x][y]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if color == 'B':
                if graph[nx][ny] == color and visit[nx][ny] == -1:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
            else:
                if graph[nx][ny] != 'B' and visit[nx][ny] == -1:
                    visit[nx][ny] = 1
                    queue.append((nx, ny))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1
    color = graph[x][y]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == color and visit[nx][ny] == -1:
                visit[nx][ny] = 1
                queue.append((nx, ny))


N = int(input())

graph = []
for _ in range(N):
    graph.append(list(input().strip()))

visit = [[-1] * N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == -1:
            bfs(i, j)
            count += 1
print(count, end=' ')
visit = [[-1] * N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == -1:
            sbfs(i, j)
            count += 1

print(count)

