# Solved on 2021.01.03
# 5-4 미로 탈출

# ---------------------------

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n = 세로길이 m = 가로길이
gamemap = []
visited = [[False] * m for _ in range(n)]
count = 0

for _ in range(n):
    gamemap.append(list(map(int, input().rstrip())))


def bfs(gamemap, x, y, visited):
    global count
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque((x, y))
    visited[x][y] = True

    while queue:
        a, b = queue.popleft()
        print(a, b)
        count += 1

        for i in range(4):
            tmp = 0
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif not visited[nx][ny] and gamemap[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append([(nx, ny)])
                tmp += 1

            if tmp == 0:
                count -= 1


bfs(gamemap, 0, 0, visited)
print(count)
