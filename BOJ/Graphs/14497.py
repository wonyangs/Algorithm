import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

graph = [[*map(str, input().strip())] for _ in range(N)]

queue = deque([(x1, y1)])
visit = [[-1] * M for _ in range(N)]
visit[x1][y1] = 0

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()
    if x == x2 and y == y2:
        print(visit[x][y])
        break
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visit[nx][ny] == -1:
            if graph[nx][ny] == '0':
                visit[nx][ny] = visit[x][y]
                queue.appendleft((nx, ny))
            else:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
