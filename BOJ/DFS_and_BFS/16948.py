# Solved on 2022. 6. 28.
# 16948 데스 나이트

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((r1, c1))
    visit = [[-1] * N for _ in range(N)]
    visit[r1][c1] = 0
    dx, dy = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

    while queue:
        x, y = queue.popleft()
        if x == r2 and y == c2:
            return visit[x][y]
        
        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
    return -1


N = int(input())
r1, c1, r2, c2 = map(int, input().split())
print(bfs())
