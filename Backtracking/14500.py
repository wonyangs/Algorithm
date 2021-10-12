# Solved on 2021. 10. 11.
# 14500 테트로미노

import sys
input = sys.stdin.readline


def DFS(x, y, depth, hap):
    global MAX
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if MAX >= hap + (4 - depth) * max_val:
        return
    if depth == 4:
        MAX = max(MAX, hap)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] is False:
            if depth == 2:
                visited[nx][ny] = True
                DFS(x, y, depth+1, hap + graph[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            DFS(nx, ny, depth+1, hap + graph[nx][ny])
            visited[nx][ny] = False


N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * M for i in range(N)]
MAX = 0
max_val = max(map(max, graph))
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, 1, graph[i][j])
        visited[i][j] = False

print(MAX)
