# Solved on 2021.01.01
# 5-3 음료수 얼려 먹기

# ---------------------------

from collections import deque
import sys
input = sys.stdin.readline


def bfs(ice, x, y, visited):
    global n, m
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif not visited[nx][ny] and ice[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True


n, m = map(int, input().split())  # n : 세로길이 m : 가로길이
ice = []
visited = [[False] * m for _ in range(n)]
count = 0

for _ in range(n):
    ice.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(m):
        if ice[i][j] == 0 and not visited[i][j]:
            bfs(ice, i, j, visited)
            count += 1

print(count)
