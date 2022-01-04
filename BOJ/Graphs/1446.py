# Solved on 2022. 1. 4.
# 1446 지름길

import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)


def dijkstra(n):
    value = [INF] * (D+1)
    queue = []
    heapq.heappush(queue, (0, n))
    value[n] = 0
    while queue:
        val, now = heapq.heappop(queue)
        for v, n in graph[now]:
            if v + val < value[n]:
                value[n] = v + val
                heapq.heappush(queue, (v+val, n))
    print(value[-1])


N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
for i in range(0, D):
    graph[i].append((1, i+1))

for _ in range(N):
    start, end, val = map(int, input().split())
    if end > D:
        continue
    graph[start].append((val, end))

dijkstra(0)
