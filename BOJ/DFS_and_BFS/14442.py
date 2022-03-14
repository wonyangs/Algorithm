# Solved on 2022. 3. 14.
# 14442 벽 부수고 이동하기 2

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visit = [[[sys.maxsize] * M for _ in range(N)] for _ in range(K+1)]
    visit[0][0][0] = 1

    while queue:
        x, y, b = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visit[b][x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0 and visit[b][nx][ny] > visit[b][x][y] + 1:
                queue.append((nx, ny, b))
                visit[b][nx][ny] = visit[b][x][y] + 1
            if graph[nx][ny] == 1 and b < K and visit[b+1][nx][ny] > visit[b][x][y] + 1:
                queue.append((nx, ny, b+1))
                visit[b+1][nx][ny] = visit[b][x][y] + 1
    return -1

N, M, K = map(int, input().split())
graph = [[*map(int, input().strip())] for _ in range(N)]
print(bfs())
