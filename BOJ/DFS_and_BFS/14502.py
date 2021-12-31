# Solved on 2021. 09. 12.
# 14502 연구소

from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline


def bfs(x, y, array):
    queue = deque()
    queue.append([x, y])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while(queue):
        v = queue.popleft()

        x, y = v

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if array[nx][ny] == 0:
                array[nx][ny] = 2
                queue.append([nx, ny])

    return array


N, M = map(int, input().split())
array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

blank = []
virus = []
for i in range(N):
    for j in range(M):
        if array[i][j] == 0:
            blank.append((i, j))
        if array[i][j] == 2:
            virus.append((i, j))


comb = list(combinations(blank, 3))

safe = []
for i in range(len(comb)):
    tmp = copy.deepcopy(array)

    ax, ay = comb[i][0]
    bx, by = comb[i][1]
    cx, cy = comb[i][2]

    tmp[ax][ay] = 1
    tmp[bx][by] = 1
    tmp[cx][cy] = 1

    for v in virus:
        tmp = bfs(v[0], v[1], tmp)

    count = 0
    for j in range(N):
        for k in range(M):
            if tmp[j][k] == 0:
                count += 1
    safe.append(count)

print(max(safe))
