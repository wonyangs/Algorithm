import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]

visit = [[False] * M for _ in range(N)]

queue = deque()
for i in range(M):
    if arr[0][i] == '0':
        queue.append((0, i))
        visit[0][i] = True

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if arr[nx][ny] == '0' and not visit[nx][ny]:
            visit[nx][ny] = True
            queue.append((nx, ny))

res = False
for i in range(M):
    if visit[-1][i]:
        res = True
print("YES" if res else "NO")
