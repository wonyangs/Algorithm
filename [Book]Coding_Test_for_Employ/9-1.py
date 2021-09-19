# Solved on 2021. 09. 19.
# 9-1 간단한 다익스트라 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for i in range(m):
    a, b, d = map(int, input().split())
    graph[a].append([b, d])


def updateDistance(node):
    visited[node] = True

    for b, d in graph[node]:
        distance[b] = min(distance[b], distance[node] + d)
    
def searchMinNode():
    MIN = INF
    MINi = 0

    for i in range(1, n+1):
        if visited[i] == False and distance[i] < MIN:
            MIN = distance[i]
            MINi = i
    return MINi

def dijkstra(start):
    distance[start] = 0
    updateDistance(start)

    for _ in range(n-1):
        node = searchMinNode()
        updateDistance(node)

dijkstra(start)
for i in range(1, n+1):
    print(distance[i])