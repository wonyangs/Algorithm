# Solved on 2021. 11. 23.
# 6593 상범 빌딩

from collections import deque
import sys
input = sys.stdin.readline


def bfs(h, x, y):
    queue = deque()
    queue.append((h, x, y))
    visit[h][x][y] = 0
    dh = [0, 0, 0, 0, 1, -1]
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0 ,0]

    while queue:
        h, x, y = queue.popleft()
        if graph[h][x][y] == 'E':
            return visit[h][x][y]
        for i in range(6):
            nh, nx, ny = h + dh[i], x + dx[i], y + dy[i]
            if 0 <= nh < L and 0 <= nx < R and 0 <= ny < C:
                if graph[nh][nx][ny] != '#' and visit[nh][nx][ny] == -1:
                    queue.append((nh, nx, ny))
                    visit[nh][nx][ny] = visit[h][x][y] + 1
    return -1


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    graph = []
    visit = [[[-1] * C for _ in range(R)] for _ in range(L)]
    for _ in range(L):
        graph.append(list(list(input().strip()) for _ in range(R)))
        input()

    for h in range(L):
        for x in range(R):
            for y in range(C):
                if graph[h][x][y] == 'S':
                    res = bfs(h, x, y)
    if res == -1:
        print('Trapped!')
    else:
        print('Escaped in', res, 'minute(s).')
