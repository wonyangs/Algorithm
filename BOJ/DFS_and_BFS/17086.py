import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
visit = [[-1] * M for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
            visit[i][j] = 0

dx, dy = [1, 1, 1, 0, 0, -1, -1, -1], [1, 0, -1, 1, -1, 1, 0, -1]

while queue:
    x, y = queue.popleft()
    
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if visit[nx][ny] == -1:
            visit[nx][ny] = visit[x][y] + 1
            queue.append((nx, ny))

res = -1
for i in range(N):
    for j in range(M):
        res = max(res, visit[i][j])
print(res)
