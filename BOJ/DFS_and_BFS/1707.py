# Solved on 2021. 10. 09.
# 1707 이분 그래프

from collections import deque
import sys
input = sys.stdin.readline


def isBipartite(num):
    for i in range(1, num+1):
        for v in graph[i]:
            if visited[i] == visited[v]:
                return False
    return True


def bfs(start):
    queue = deque()
    queue.append(start)
    if visited[start] == -1:
        visited[start] = 0

    while queue:
        now = queue.popleft()

        for v in graph[now]:
            if visited[v] == -1:
                if visited[now] == 0:
                    visited[v] = 1
                elif visited[now] == 1:
                    visited[v] = 0
                queue.append(v)


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    visited = [-1] * (V+1)
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V+1):
        bfs(i)

    if isBipartite(V):
        print('YES')
    else:
        print('NO')
