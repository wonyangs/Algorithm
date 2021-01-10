# Solved on 2021.01.05
# 1012 유기농 배추 ver.BFS

# ---------------------------

from collections import deque
import sys
input = sys.stdin.readline


def bfs(field, x, y, visited):
    visited[x][y] = True
    queue = deque()
    queue.append([x, y])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif field[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])


T = int(input())  # T = 테스트 케이스의 개수

for _ in range(T):
    m, n, k = map(int, input().split())  # m = 가로 n = 세로 k = 배추개수
    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        a, b = map(int, input().split())
        field[b][a] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and not visited[i][j]:
                bfs(field, i, j, visited)
                count += 1

    print(count)
