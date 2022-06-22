# Solved on 2022. 6. 22.
# 21610 마법사 상어와 비바라기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
clouds = {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}
dir = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

for _ in range(M):
    d, s = map(int, input().split())

    new_clouds = set()
    for cloud in clouds:
        x = (cloud[0] + dir[d][0] * s + N) % N
        y = (cloud[1] + dir[d][1] * s + N) % N
        new_clouds.add((x, y))
        graph[x][y] += 1
    clouds = new_clouds

    update = []
    for cloud in clouds:
        count = 0
        for dx, dy in [dir[2], dir[4], dir[6], dir[8]]:
            nx, ny = cloud[0] + dx, cloud[1] + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] > 0:
                count += 1
        update.append((cloud[0], cloud[1], count))
    for x, y, n in update:
        graph[x][y] += n

    new_clouds = set()
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and (i, j) not in clouds:
                new_clouds.add((i, j))
                graph[i][j] -= 2
    clouds = new_clouds

total = 0
for i in range(N):
    for j in range(N):
        total += graph[i][j]
print(total)
