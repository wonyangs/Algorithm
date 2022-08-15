from collections import deque

def bfs(x, y):
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

            if visit[nx][ny] is False and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visit[nx][ny] = True
                count += 1
    return count


N, M, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
visit = [[False] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

res = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visit[i][j] is False:
            res = max(res, bfs(i, j))
print(res)
