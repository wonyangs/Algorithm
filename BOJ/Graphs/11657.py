# Solved on 2022. 1. 6.
# 11657 타임머신

import sys
input = sys.stdin.readline
INF = int(1e9)


def BF(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            node, next_node, cost = edges[j][0], edges[j][1], edges[j][2]
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                if i == N-1:
                    print(-1)
                    return
    for i in range(2, N+1):
        print(dist[i] if dist[i] != INF else -1)


N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
BF(1)
