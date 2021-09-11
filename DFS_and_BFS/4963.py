# Solved on 2021. 09. 11.
# 4963 섬의 개수

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y, graph):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False

    dx = [1, 1, -1, -1, 0, 0, 1, -1]
    dy = [1, -1, 1, -1, 1, -1, 0, 0]

    if graph[x][y] == 1:
        graph[x][y] = 0

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, graph)
        return True
    return False


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    result = 0
    for i in range(w):
        for j in range(h):
            if dfs(j, i, graph):
                result += 1

    print(result)
