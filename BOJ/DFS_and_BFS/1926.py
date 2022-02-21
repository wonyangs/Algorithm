# Solved on 2022. 2. 21.
# 1926 그림

from collections import deque
import sys
input = sys.stdin.readline   

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    count = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 1 and not visit[nx][ny]:
                queue.append((nx, ny))
                visit[nx][ny] = True
                count += 1
    return count

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
visit = [[False] * M for _ in range(N)]

pic = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visit[i][j]:
            pic.append(bfs(i, j))
print(len(pic))
pic.append(0)
print(max(pic))
