# Solved on 2021. 11. 10.
# 2636 치즈

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visit = [[False] * W for _ in range(H)]
    arr = []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                continue
            if visit[nx][ny] == False and graph[nx][ny] == 0:
                queue.append((nx, ny))
                visit[nx][ny] = True
            if visit[nx][ny] == False and graph[nx][ny] == 1:
                arr.append((nx, ny))
                visit[nx][ny] = True
    for x, y in arr:
        graph[x][y] = 0
    return len(arr)


H, W = map(int, input().split())
graph = []
for _ in range(H):
    graph.append(list(map(int, input().split())))

isChange = True
count = 0
tmp = 0
while True:
    isChange = bfs(0, 0)
    if isChange != 0:
        tmp = isChange
        count += 1
    else:
        print(count)
        print(tmp)
        break
