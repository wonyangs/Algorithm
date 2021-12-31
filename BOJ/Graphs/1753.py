# Solved on 2021. 09. 19.
# 1753 최단경로

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = i[1] + distance[now]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(K)
for i in range(1, V+1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print('INF')
