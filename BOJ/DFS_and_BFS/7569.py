# Solved on 2021. 11. 22.
# 7569 토마토

from collections import deque
import sys
input = sys.stdin.readline


def bfs(arr):
    queue = deque()
    for h, x, y in arr:
        queue.append((h, x, y))
        visit[h][x][y] = 0
    dh = [0, 0, 0, 0, 1, -1]
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]

    while queue:
        h, x, y = queue.popleft()
        for i in range(6):
            nh, nx, ny = h + dh[i], x + dx[i], y + dy[i]
            if nh < 0 or nh >= H or nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visit[nh][nx][ny] == -1 and graph[nh][nx][ny] == 0:
                queue.append((nh, nx, ny))
                visit[nh][nx][ny] = visit[h][x][y] + 1
    MAX = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    if visit[i][j][k] == -1:
                        return -1
                    MAX = max(MAX, visit[i][j][k])
    return MAX


M, N, H = map(int, input().split())
graph = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]
visit = [[[-1] * M for _ in range(N)] for _ in range(H)]

change = []
for h in range(H):
    for x in range(N):
        for y in range(M):
            if graph[h][x][y] == 1:
                change.append((h, x, y))
print(bfs(change))
