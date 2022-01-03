# Solved on 2022. 1. 3.
# 7562 나이트의 이동

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, fx, fy, L):
    queue = deque()
    queue.append((x, y))
    visit = [[0] * L for _ in range(L)]
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    
    while queue:
        x, y = queue.popleft()
        if x == fx and y == fy:
            return visit[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= L or ny >= L:
                continue
            if visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))


T = int(input())
for _ in range(T):
    L = int(input())
    x, y = map(int, input().split())
    fx, fy = map(int, input().split())
    print(bfs(x, y, fx, fy, L))
