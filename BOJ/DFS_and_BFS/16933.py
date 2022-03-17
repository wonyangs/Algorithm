# Solved on 2022. 3. 17.
# 16933 벽 부수고 이동하기 3

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visit = [[[0] * M for _ in range(N)] for _ in range(K+1)]
    visit[0][0][0] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    day = True
    count = 0

    while queue:
        count += 1
        for _ in range(len(queue)):
            x, y, k = queue.popleft()
            if x == N-1 and y == M-1:
                return visit[k][x][y]
            
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                
                if not visit[k][nx][ny] and graph[nx][ny] == 0:
                    queue.append((nx, ny, k))
                    visit[k][nx][ny] = count + 1
                
                if k < K and not visit[k+1][nx][ny] and graph[nx][ny] == 1:
                    if not day:
                        queue.append((x, y, k))
                    else:
                        queue.append((nx, ny, k+1))
                        visit[k+1][nx][ny] = count + 1
        day = not day
    return -1

N, M, K = map(int, input().split())
graph = [[*map(int, input().strip())] for _ in range(N)]
print(bfs())
