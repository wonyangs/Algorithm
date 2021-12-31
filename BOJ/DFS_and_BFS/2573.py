# Solved on 2021. 11. 15.
# 2573 빙산

from collections import deque
import sys
input = sys.stdin.readline


def checkMountain(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True
    dx = [1, -1, 0 ,0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visit[nx][ny] is False and graph[nx][ny] != 0:
                visit[nx][ny] = True
                queue.append((nx, ny))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True
    dx = [1, -1, 0 ,0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for j in range(4):
            tx = x + dx[j]
            ty = y + dy[j]
            if tx < 0 or ty < 0 or tx >= N or ty >= M:
                continue
            if graph[tx][ty] != 0:
                res.append((tx, ty))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visit[nx][ny] is False and graph[nx][ny] == 0:
                visit[nx][ny] = True
                queue.append((nx, ny))


N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

count = 0
while True:
    isWork = False
    visit = [[False] * M for _ in range(N)]
    res = []
    for i in range(N):
        for j in range(M):
            if visit[i][j] is False and graph[i][j] == 0:
                bfs(i, j)
    for x, y in res:
        if graph[x][y] > 0:
            graph[x][y] -= 1
            isWork = True
    if isWork is False:
        print(0)
        break
    count += 1
    visit = [[False] * M for _ in range(N)]
    isBreak = False
    end = False
    for i in range(N):
        for j in range(M):
            if end is False and visit[i][j] is False and graph[i][j] != 0:
                if isBreak == True:
                    end = True
                checkMountain(i, j)
                isBreak = True
    if end:
        print(count)
        break
