# Solved on 2021.01.04
# 2667 단지번호붙이기 ver.BFS

# ---------------------------

from collections import deque
import sys
input = sys.stdin.readline


def bfs(board, x, y, visited):
    global count

    queue = deque()
    queue.append((x, y))

    visited[x][y] = True
    count += 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            elif not visited[nx][ny] and board[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1


n = int(input())
board = []
visited = [[False] * n for _ in range(n)]
count = 0
num = 0
c = []


for _ in range(n):
    board.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(board, i, j, visited)
            c.append(count)
            count = 0
            num += 1

print(num)
c.sort()
for i in c:
    print(i)
