import sys
import heapq

input = sys.stdin.readline

graph = [[0] * 501 for _ in range(501)]
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a, c = min(a, c), max(a, c)
    b, d = min(b, d), max(b, d)
    
    for i in range(a, c+1):
        for j in range(b, d+1):
            graph[i][j] = 1

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a, c = min(a, c), max(a, c)
    b, d = min(b, d), max(b, d)
    
    for i in range(a, c+1):
        for j in range(b, d+1):
            graph[i][j] = 2

hq = [(0, 0, 0)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visit = [[float('inf')] * 501 for _ in range(501)]
visit[0][0] = 0
while hq:
    w, x, y = heapq.heappop(hq)
    if x == 500 and y == 500:
        continue
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx > 500 or ny < 0 or ny > 500:
            continue
        if graph[nx][ny] == 2:
            continue
        
        nxt_w = w + graph[nx][ny]
        if visit[nx][ny] > nxt_w:
            visit[nx][ny] = nxt_w
            heapq.heappush(hq, (nxt_w, nx, ny))

print(-1 if visit[-1][-1] == float('inf') else visit[-1][-1])
