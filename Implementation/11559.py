# Solved on 2021. 11. 12.
# 11559 Puyo Puyo

from collections import deque
import sys
input = sys.stdin.readline


def drop():
    for i in range(11, -1, -1):
        for j in range(6):
            if graph[i][j] == '.':
                for k in range(i-1, -1, -1):
                    if graph[k][j] != '.':
                        graph[i][j] = graph[k][j]
                        graph[k][j] = '.'
                        break


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    res = []
    res.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6:
                continue
            if visit[nx][ny] is False and graph[nx][ny] == graph[x][y]:
                visit[nx][ny] = True
                queue.append((nx, ny))
                res.append((nx, ny))

    return res


graph = []
for _ in range(12):
    graph.append(list(input().strip()))

count = 0
while True:
    visit = [[False] * 6 for _ in range(12)]
    blocks = []
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and visit[i][j] is False:
                arr = bfs(i, j)
                blocks.append(arr)

    isBoom = False
    for arr in blocks:
        if len(arr) >= 4:
            isBoom = True
            for x, y in arr:
                graph[x][y] = '.'
    
    drop()
    if isBoom is False:
        break
    else:
        count += 1

print(count)
