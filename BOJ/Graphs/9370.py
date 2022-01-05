# Solved on 2022. 1. 5.
# 9370 미확인 도착지

import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)


def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        d, now = heapq.heappop(queue)
        for nd, nxt in graph[now]:
            if dist[nxt] > d + nd:
                dist[nxt] = d + nd
                heapq.heappush(queue, (d+nd, nxt))
    return dist

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g):
            must = d
        graph[a].append((d, b))
        graph[b].append((d, a))
    candidate = [int(input()) for _ in range(t)]
    
    startDist = dijkstra(s)
    gDist = dijkstra(g)
    hDist = dijkstra(h)
    
    res = []
    for node in candidate:
        dist = startDist[node]
        if startDist[g] + must + hDist[node] == dist or startDist[h] + must + gDist[node] == dist:
            res.append(node) 

    res.sort()
    for n in res:
        print(n, end = ' ')
    print()
