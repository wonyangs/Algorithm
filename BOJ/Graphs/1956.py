# Solved on 2022. 1. 7.
# 1956 운동

from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (V+1)
    distance[start] = 0
    pq = []
    heappush(pq, (0, start))
    while pq:
        d, now = heappop(pq)
        for nxt, dist in graph[now]:
            cost = dist + d
            if distance[nxt] == 0:
                distance[nxt] = cost
            elif distance[nxt] > cost:
                distance[nxt] = cost
                heappush(pq, (cost, nxt))
    if distance[start] != 0:
        return distance[start]
    else:
        return INF


V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

res = []
for i in range(1, V+1):
    res.append(dijkstra(i))
r = min(res)
print(r if r != 0 and r != INF else -1)
