# Solved on 2022. 2. 23.
# 5427 불

from collections import deque
import sys
input = sys.stdin.readline   

def bfs(graph):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = deque()
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '*':
                queue.append((i, j))
    fire_graph = [[-1] * W for _ in range(H)]
    for x, y in queue:
        fire_graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                continue
            if graph[nx][ny] != '#' and fire_graph[nx][ny] == -1:
                fire_graph[nx][ny] = fire_graph[x][y] + 1
                queue.append((nx, ny))
    
    visit = [[-1]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '@':
                queue.append((i, j))
                visit[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                print(visit[x][y]+1)
                return
            if graph[nx][ny] == '.' and visit[nx][ny] == -1 and (fire_graph[nx][ny] > visit[x][y]+1 or fire_graph[nx][ny] == -1):
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
    print('IMPOSSIBLE')
    return
   

T = int(input())
for _ in range(T):
    W, H = map(int, input().split())
    graph = [[*map(str, input().strip())] for _ in range(H)]
    bfs(graph)
