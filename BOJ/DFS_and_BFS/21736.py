from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

x, y = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            x, y = i, j
            
queue = deque()
visit = [[False] * M for _ in range(N)]
visit[x][y] = True
queue.append((x, y))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
res = 0
while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not visit[nx][ny] and arr[nx][ny] != 'X':
            queue.append((nx, ny))
            visit[nx][ny] = True
            if arr[nx][ny] == 'P':
                res += 1
print(res if res else "TT")
