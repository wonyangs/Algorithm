# Solved on 2021. 11. 08.
# 2589 보물섬

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit = [[-1] * b for _ in range(a)]
    visit[x][y] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    MAX = 0
    while queue:
        x, y = queue.popleft()
        if visit[x][y] > MAX:
            MAX = visit[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= a or ny >= b:
                continue
            if graph[nx][ny] == 'L' and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
    return MAX


a, b = map(int, input().split())

graph = []
for _ in range(a):
    graph.append(list(input().strip()))

arr = []
for i in range(a):
    for j in range(b):
        if graph[i][j] == 'L':
            n = bfs(i, j)
            arr.append(n)

print(max(arr))
