from collections import deque

def bfs(x, y, c):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    count = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == c and visit[nx][ny] is False:
                queue.append((nx, ny))
                visit[nx][ny] = True
                count += 1
    return count

M, N = map(int, input().split())
graph = [[*map(str, input().strip())] for _ in range(N)]
visit = [[False] * M for _ in range(N)]
blue, white = 0, 0
for i in range(N):
    for j in range(M):
        if visit[i][j] is False:
            cnt = bfs(i, j, graph[i][j])
            if graph[i][j] == 'B':
                blue += cnt ** 2
            else:
                white += cnt ** 2

print(white, blue)
