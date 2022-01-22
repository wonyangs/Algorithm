# Solved on 2022. 1. 22.
# 4485 녹색 옷 입은 애가 젤다지?

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(x, y):
    queue = []
    distance = [[INF] * N for _ in range(N)]
    distance[x][y] = graph[x][y]
    heapq.heappush(queue, (distance[x][y], x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        dist, x, y = heapq.heappop(queue)
        if x == N-1 and y == N-1:
            return dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            
            if graph[nx][ny] + dist < distance[nx][ny]:
                distance[nx][ny] = graph[nx][ny] + dist
                heapq.heappush(queue, (distance[nx][ny], nx, ny))


count = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    graph = [[*map(int, input().split())] for _ in range(N)]
    res = dijkstra(0, 0)
    print("Problem %d: %d"%(count, res))
    count += 1
