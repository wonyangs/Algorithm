# Solved on 2021. 11. 16.
# 17142 연구소 3

from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


def bfs(arr):
    queue = deque()
    visit = [[-1] * N for _ in range(N)]
    for x, y in arr:
        queue.append((x, y))
        visit[x][y] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visit[nx][ny] == -1 and graph[nx][ny] != 1:
                queue.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1

    check = True
    for i in range(N):
        for j in range(N):
            if visit[i][j] == -1 and graph[i][j] == 0:
                check = False
    if check is False:
        return -1

    MAX = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                MAX = max(MAX, visit[i][j])

    return MAX


N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i, j))

virusCom = list(combinations(virus, M))
MIN = int(10e9)
for arr in virusCom:
    m = bfs(arr)
    if m == -1:
        continue
    MIN = min(m, MIN)

if MIN == int(10e9):
    print(-1)
else:
    print(MIN)
