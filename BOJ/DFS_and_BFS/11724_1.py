# Solved on 2021. 01. 10.
# 11724 연결 요소의 개수 ver.BFS


from collections import deque
import sys
input = sys.stdin.readline


def BFS(graph, n, visited):
    visited[n] = True
    queue = deque()
    queue.append(n)
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


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
        BFS(graph, i, visited)

print(count)
