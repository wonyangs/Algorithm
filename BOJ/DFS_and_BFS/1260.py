# Solved on 2021.01.04
# 1260 DFS와 BFS

# ---------------------------

from collections import deque
import sys
input = sys.stdin.readline


def init_visited():
    visited = [False] * (n+1)

    return visited


def dfs(graph, n, visited):
    visited[n] = True
    print(n, end=' ')

    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, n, visited):
    visited[n] = True
    queue = deque([n])

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())  # n = 정점의 개수 m = 간선의 개수 v = 탐색 시작 번호
graph = [[] for _ in range(n+1)]

for _ in range(m):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

for i in range(1, n+1):
    graph[i].sort()

visited = init_visited()
dfs(graph, v, visited)
print()
visited = init_visited()
bfs(graph, v, visited)
