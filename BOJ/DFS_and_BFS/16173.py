# Solved on 2022. 5. 6.
# 16173 점프왕 쩰리 (Small)

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [[*map(int, input().split())] for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0, 0))
    dx, dy = [1, 0], [0, 1]
    visit = [[False] * N for _ in range(N)]
    visit[0][0] = True

    while queue:
        x, y = queue.popleft()
        length = graph[x][y]
        if length == -1:
            return True

        for i in range(2):
            nx, ny = x+dx[i]*length, y+dy[i]*length
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] is False:
                queue.append((nx, ny))
                visit[nx][ny] = True
                
    return False
            

if bfs():
    print("HaruHaru")
else:
    print("Hing")
