# Solved on 2021. 01. 10.
# 11724 연결 요소의 개수 ver.DFS


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def DFS(graph, n, visited):
    visited[n] = True
    
    for i in graph[n]:
        if not visited[i]:
            DFS(graph, i, visited)


n, m = map(int, input().split())  # n : 정점의 개수  m : 간선의 개수
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(graph, i, visited)

print(count)
