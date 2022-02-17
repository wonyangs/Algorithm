# Solved on 2022. 2. 17.
# 19238 스타트 택시

from collections import deque
import sys
input = sys.stdin.readline


def next_start():
    queue = deque()
    queue.append((taxi_x, taxi_y))
    visit = [[-1] * N for _ in range(N)]
    visit[taxi_x][taxi_y] = 0
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] != 1 and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
    
    res = []
    for i in range(M):
        if i not in visit_node:
            x, y = start_info[i]
            res.append((visit[x][y], i))
    res.sort()
    return res[0]


def bfs(start_x, start_y, end_x, end_y):
    queue = deque()
    queue.append((start_x, start_y))
    visit = [[-1] * N for _ in range(N)]
    visit[start_x][start_y] = 0
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            return visit[x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] != 1 and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
    return -1


N, M, feul = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
taxi_x, taxi_y = map(int, input().split())
taxi_x -= 1
taxi_y -= 1
start_info, finish_info = [], []
info = [[*map(int, input().split())] for _ in range(M)]
info.sort()
for a, b, c, d in info:
    start_info.append((a-1, b-1))
    finish_info.append((c-1, d-1))
visit_node = set()

while len(visit_node) != M:
    dist, nxt_node = next_start()
    if dist > feul or dist == -1:
        print(-1)
        sys.exit(0)
    feul -= dist
    taxi_x, taxi_y = start_info[nxt_node]
    
    dist = bfs(taxi_x, taxi_y, finish_info[nxt_node][0], finish_info[nxt_node][1])
    if dist > feul:
        print(-1)
        sys.exit(0)
    feul -= dist
    feul += dist * 2
    taxi_x, taxi_y = finish_info[nxt_node]
    visit_node.add(nxt_node)
    
print(feul)
