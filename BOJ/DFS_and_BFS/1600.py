# Solved on 2022. 2. 18.
# 1600 말이 되고픈 원숭이

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append([0, 0, 0, 0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    hx = [-2, -1, 1, 2, 2, 1, -1, -2]
    hy = [-1, -2, -2, -1, 1, 2, 2, 1]
    visit = [[[False] * W for _ in range(H)] for _ in range(K+1)]
    
    while queue:
        x, y, count, h = queue.popleft()
        if x == H-1 and y == W-1:
            print(count)
            return
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                continue
            if not visit[h][nx][ny] and graph[nx][ny] != 1:
                queue.append([nx, ny, count+1, h])
                visit[h][nx][ny] = True
        
        if h + 1 > K:
            continue
        for i in range(8):
            nx, ny = x+hx[i], y+hy[i]
            if nx < 0 or ny < 0 or nx >= H or ny >= W:
                continue
            if not visit[h+1][nx][ny] and graph[nx][ny] != 1:
                queue.append([nx, ny, count+1, h+1])
                visit[h+1][nx][ny] = True
    print(-1)
    return


K = int(input())
W, H = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(H)]
bfs()
