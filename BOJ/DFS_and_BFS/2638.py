# Solved on 2022. 2. 9.
# 2638 치즈

from collections import deque
import sys
input = sys.stdin.readline


def cheese():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                return True
    return False


def bfs():
    queue = deque()
    queue.append((0, 0))
    visit = [[0] * M for _ in range(N)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visit[nx][ny] == 0 and graph[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append((nx, ny))
            elif graph[nx][ny] == 1:
                visit[nx][ny] += 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visit[i][j] >= 2:
                graph[i][j] = 0


N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]

time = 0
while cheese():
    time += 1
    bfs()
print(time)
