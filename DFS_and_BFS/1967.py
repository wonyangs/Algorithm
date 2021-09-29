# Solved on 2021. 09. 29.
# 1967 트리의 지름

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))


def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [-1] * (n+1)
    visited[start] = 0

    while queue:
        now = queue.popleft()

        for x, cost in graph[now]:
            if visited[x] == -1:
                visited[x] = visited[now] + cost
                queue.append(x)
    return visited


arr = bfs(1)
result = bfs(arr.index(max(arr)))
print(max(result))



