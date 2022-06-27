# Solved on 2022. 6. 27.
# 3184 양

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    sheep = 0
    wolf = 0

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if not visit[nx][ny] and graph[nx][ny] != '#':
                queue.append((nx, ny))
                visit[nx][ny] = True
                if graph[nx][ny] == 'o':
                    sheep += 1
                if graph[nx][ny] == 'v':
                    wolf += 1
    if wolf == 0 and sheep == 0:
        return 0
    if sheep > wolf:
        return sheep
    else:
        return -wolf


R, C = map(int, input().split())
graph = [[*map(str, input().strip())] for _ in range(R)]
visit = [[False] * C for _ in range(R)]
sheep = 0
wolf = 0

for i in range(R):
    for j in range(C):
        if not visit[i][j]:
            res = bfs(i, j)
            if res < 0:
                wolf += -res
            else:
                sheep += res

print(sheep, wolf)
