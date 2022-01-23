# Solved on 2022. 1. 23.
# 2665 미로만들기

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra():
    queue = []
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = 0
    heapq.heappush(queue, (distance[0][0], 0, 0))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        dist, x, y = heapq.heappop(queue)
        if x == N-1 and y == N-1:
            return dist
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            val = abs(graph[x][y] - 1)
            if distance[nx][ny] > dist + val:
                distance[nx][ny] = dist + val
                heapq.heappush(queue, (distance[nx][ny], nx, ny))


N = int(input())
graph = [[*map(int, input().strip())] for _ in range(N)]
print(dijkstra())
