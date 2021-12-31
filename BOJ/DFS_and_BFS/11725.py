# Solved on 2021. 09. 21.
# 11725 트리의 부모 찾기

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [-1] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    queue = deque()
    queue.append(start)
    parent[start] = 0

    while queue:
        now = queue.pop()

        for x in graph[now]:
            if parent[x] == -1:
                parent[x] = now
                queue.append(x)


bfs(1)
for i in parent[2:]:
    print(i)
