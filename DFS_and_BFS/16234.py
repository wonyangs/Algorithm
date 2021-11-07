# Solved on 2021. 11. 07.
# 16234 인구 이동

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, count):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = count
    un = []
    un.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or nx >= N or ny >= N:
                continue

            k = abs(graph[x][y] - graph[nx][ny])
            if L <= k <= R and visit[nx][ny] == 0:
                queue.append((nx, ny))
                visit[nx][ny] = count
                un.append((nx, ny))
    return un


N, L, R = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

days = 0
while True:
    visit = [[0] * N for _ in range(N)]
    count = 1
    un = []
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                arr = bfs(i, j, count)
                un.append(arr)
                count += 1

    move = False
    for arr in un:
        if len(arr) < 2:
            continue
        hap = 0
        for x, y in arr:
            hap += graph[x][y]
        res = hap // len(arr)
        for x, y in arr:
            graph[x][y] = res
        move = True
    if move is False:
        break
    days += 1

print(days)
