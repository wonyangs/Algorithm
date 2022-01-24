# Solved on 2022. 1. 24.
# 1238 파티

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(graph, start):
    queue = []
    distance = [INF] * (N+1)
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for n, d in graph[now]:
            if distance[n] > dist + d:
                distance[n] = dist + d
                heapq.heappush(queue, (distance[n], n))
    return distance[1:]


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    rev_graph[b].append((a, c))
X_to_all = dijkstra(graph, X)
all_to_X = dijkstra(rev_graph, X)
print(max(X_to_all[i] + all_to_X[i] for i in range(1, N)))
