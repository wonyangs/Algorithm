# Solved on 2022. 2. 22.
# 4179 불!

from collections import deque
import sys
input = sys.stdin.readline   

def new_fire(arr):
    global fire_graph
    queue = deque()
    for x, y in arr:
        queue.append((x, y))
    fire_graph[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if graph[nx][ny] != '#' and fire_graph[nx][ny] == -1:
                queue.append((nx, ny))
                fire_graph[nx][ny] = fire_graph[x][y] + 1

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit = [[-1]*C for _ in range(R)]
    visit[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                print(visit[x][y]+1)
                return
            if graph[nx][ny] == '.' and visit[nx][ny] == -1 and (fire_graph[nx][ny] > visit[x][y] + 1 or fire_graph[nx][ny]==-1):
                queue.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
    print('IMPOSSIBLE')
    
    return

R, C = map(int, input().split())
graph = [[*map(str, input().strip())] for _ in range(R)]
fire_graph = [[-1] * C for _ in range(R)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
fires = set()
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            fires.add((i,j))
if len(fires):
    new_fire(fires)
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            bfs(i, j)