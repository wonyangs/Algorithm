# Solved on 2021. 09. 12.
# 2206 벽 부수고 이동하기

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    array.append(list(map(int, input().strip())))


def bfs(x, y, crush, array, visited):
    queue = deque()
    queue.append([x, y, crush])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited[x][y][crush] = 1

    while queue:
        x, y, crush = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][crush]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if array[nx][ny] == 0 and visited[nx][ny][crush] == 0:
                queue.append([nx, ny, crush])
                visited[nx][ny][crush] = visited[x][y][crush] + 1
            if array[nx][ny] == 1 and crush == 0:
                queue.append([nx, ny, crush+1])
                visited[nx][ny][crush+1] = visited[x][y][crush] + 1
    return -1


print(bfs(0, 0, 0, array, visited))
