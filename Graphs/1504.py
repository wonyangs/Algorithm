# Solved on 2021. 09. 20.
# 1504 특정한 최단 경로

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())

    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())


def dijkstra(start, end):
    q = []
    distance = [INF] * (N+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]


v1Result = dijkstra(1, v1) + dijkstra(v2, N)
v2Result = dijkstra(1, v2) + dijkstra(v1, N)
result = dijkstra(v1, v2) + min(v1Result, v2Result)

if result >= INF:
    print(-1)
else:
    print(result)
