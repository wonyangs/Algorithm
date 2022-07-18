# Solved on 2022. 7. 18.
# 18170 두 동전 언리미티드

from collections import deque
import sys
input = sys.stdin.readline


def is_in_graph(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False


def bfs(ax, ay, bx, by):
    queue = deque()
    queue.append((ax, ay, bx, by, 0))
    visit = set()
    visit.add((ax, ay, bx, by))
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        ax, ay, bx, by, n = queue.popleft()

        for i in range(4):
            nax, nay = ax + dx[i], ay + dy[i]
            if is_in_graph(nax, nay) and graph[nax][nay] == '#':
                nax, nay = ax, ay
            nbx, nby = bx + dx[i], by + dy[i]
            if is_in_graph(nbx, nby) and graph[nbx][nby] == '#':
                nbx, nby = bx, by

            if (nax, nay, nbx, nby) in visit or (not is_in_graph(nax, nay) and not is_in_graph(nbx, nby)):
                continue

            if is_in_graph(nax, nay) and not is_in_graph(nbx, nby):
                return n + 1
            elif not is_in_graph(nax, nay) and is_in_graph(nbx, nby):
                return n + 1
            else:
                visit.add((nax, nay, nbx, nby))
                queue.append((nax, nay, nbx, nby, n + 1))
    return -1


N, M = map(int, input().split())
graph = [[*map(str, input().strip())] for _ in range(N)]

ax, ay, bx, by = -1, -1, -1, -1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'o':
            if ax == -1:
                ax, ay = i, j
            else:
                bx, by = i, j

print(bfs(ax, ay, bx, by))
