# Solved on 2021. 09. 26.
# 1865 웜홀

import sys
input = sys.stdin.readline
INF = int(1e9)


def bf(dist, graph, n):
    for i in range(n):
        for j in range(len(graph)):
            now = graph[j][0]
            nextNode = graph[j][1]
            cost = graph[j][2]

            if dist[nextNode] > dist[now] + cost:
                dist[nextNode] = dist[now] + cost

                if i == n-1:
                    return True
    return False


TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = []
    distance = [0] * (N+1)

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph.append([S, E, T])
        graph.append([E, S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        graph.append([S, E, -T])

    if bf(distance, graph, N):
        print("YES")
    else:
        print("NO")

