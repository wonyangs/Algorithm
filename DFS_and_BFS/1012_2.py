# Solved on 2021.01.05
# 1012 유기농 배추 ver.DFS

# ---------------------------

import sys
input = sys.stdin.readline


def dfs(field, x, y, visited):
    if x < 0 or y < 0 or x >= n or y >= m:
        return

    if not visited[x][y] and field[x][y] == 1:
        visited[x][y] = True

        dfs(field, x-1, y, visited)
        dfs(field, x+1, y, visited)
        dfs(field, x, y-1, visited)
        dfs(field, x, y+1, visited)


T = int(input())  # T = 테스트 케이스의 개수

for _ in range(T):
    m, n, k = map(int, input().split())  # m = 가로 n = 세로 k = 배추개수
    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        a, b = map(int, input().split())
        field[b][a] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(field, i, j, visited)
                count += 1

    print(count)
