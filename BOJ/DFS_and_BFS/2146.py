# Solved on 2022. 2. 1.
# 2146 다리 만들기

from collections import deque
import sys
input = sys.stdin.readline


def edge():
    islands = []
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and not visit[i][j]:
                islands.append(island_bfs(i, j, visit))
    return islands


def island_bfs(x, y, visit):
    queue = deque()
    queue.append((x, y))
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visit[x][y] = True
    island_set = set()
    island_set.add((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny))
                island_set.add((nx, ny))
                
    return island_set


def bfs(island):
    queue = deque()
    visit = [[1000] * N for _ in range(N)]
    for x, y in island:
        queue.append((x, y))
        visit[x][y] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 0 and visit[nx][ny] > visit[x][y] + 1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
            if graph[nx][ny] == 1 and (nx, ny) not in island:
                return visit[x][y] - 1
    return 1000

def dari(islands):
    res = []
    for island in islands:
        res.append(bfs(island))
    print(min(res))

N = int(input())
graph = [[*map(int, input().split())] for _ in range(N)]
dari(edge())
