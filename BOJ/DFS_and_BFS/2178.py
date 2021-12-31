# Solved on 2021.01.05
# 2178 미로 탐색

# ---------------------------

from collections import deque
import sys
input = sys.stdin.readline


def bfs(field, x, y):
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
            elif field[nx][ny] == 1:
                queue.append([nx, ny])
                field[nx][ny] = field[x][y] + 1


n, m = map(int, input().split())  # n = 세로길이 m = 가로길이
field = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    field.append(list(map(int, input().rstrip())))

bfs(field, 0, 0)

print(field[n-1][m-1])
print(field)
