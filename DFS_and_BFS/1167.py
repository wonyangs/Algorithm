# Solved on 2021. 09. 30.
# 1167 트리의 지름

from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    arr = list(map(int, input().split()))
    a = arr[0]

    for i in range(2, len(arr), 2):
        b = arr[i-1]
        c = arr[i]
        graph[a].append((b, c))


def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [-1] * (v+1)
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
