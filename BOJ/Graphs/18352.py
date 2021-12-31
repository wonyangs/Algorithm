# Solved on 2021. 11. 06.
# 18352 특정 거리의 도시 찾기

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dist = [INF] * (N+1)
    dist[start] = 0
    
    while queue:
        d, now = heapq.heappop(queue)

        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = dist[now] + 1
            if cost < dist[i]:
                dist[i] = cost
                heapq.heappush(queue, (cost, i))

    isPrint = False
    for i in range(1, N+1):
        if dist[i] == K:
            isPrint = True
            print(i)

    if isPrint is False:
        print(-1)


N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

dijkstra(X)
