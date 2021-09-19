# Solved on 2021. 09. 19.
# 9-5 전보

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())

distance = [INF] * (N+1)

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        for i, j in graph[now]:
            if distance[i] > j + distance[now]:
                distance[i] = j + distance[now]
                heapq.heappush(q, (distance[i], i))

dijkstra(C)

count = 0
MAX = -1
for i in range(1, N+1):
    if distance[i] < INF:
        count += 1
        MAX = max(MAX, distance[i])

print(count-1, MAX)