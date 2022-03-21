# Solved on 2022. 3. 21.
# 11967 불켜기

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((0, 0))
    visit = set()
    visit.add((0, 0))
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    lig = False

    while queue:
        x, y = queue.popleft()
        while len(light[(x, y)]):
            i, j = light[(x, y)].pop()
            graph[i][j] = 1
            lig = True
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if (nx, ny) not in visit and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visit.add((nx, ny))
    return lig

N, M = map(int, input().split())
light = defaultdict(list)
graph = [[0] * N for _ in range(N)]
graph[0][0] = 1

for _ in range(M):
    x, y, a, b = map(int, input().split())
    light[(x-1, y-1)].append((a-1, b-1))

res = True
while res:
    res = bfs()

count = 0
for i in range(N):
    for j in range(N):
        count += graph[i][j]
print(count)
