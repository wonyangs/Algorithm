from collections import deque

N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]

res = [[-1] * M for _ in range(N)]

sx, sy = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            res[i][j] = 0
        elif arr[i][j] == 2:
            sx, sy = i, j
            res[i][j] = 0

queue = deque()
queue.append((sx, sy))
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        
        if res[nx][ny] == -1:
            res[nx][ny] = res[x][y] + 1
            queue.append((nx, ny))

for r in res:
    print(*r)
