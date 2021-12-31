# Solved on 2021. 10. 13.
# 1987 알파벳

import sys
input = sys.stdin.readline


def bfs(x, y):
    queue = set([(x, y, graph[x][y])])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    MAX = 0
    while queue:
        x, y, visit = queue.pop()
        if MAX < len(visit):
            MAX = len(visit)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if graph[nx][ny] not in visit:
                queue.add((nx, ny, visit+graph[nx][ny]))
    print(MAX)


R, C = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(list(input().strip()))

bfs(0, 0)