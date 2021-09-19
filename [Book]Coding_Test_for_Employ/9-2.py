# Solved on 2021. 09. 19.
# 9-2 개선된 다익스트라 알고리즘

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b, d = map(int, input().split())
    graph[a].append([b, d])


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist:
            continue

        for b, d in graph[node]:
            if distance[b] > distance[node] + d:
                distance[b] = distance[node] + d
                heapq.heappush(q, (d, b))


dijkstra(start)
for i in range(1, n+1):
    print(distance[i])