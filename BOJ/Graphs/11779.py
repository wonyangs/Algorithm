import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
distance = [(int(1e9), ())] * (N + 1)

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

S, E = map(int, input().split())

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = (0, (start,))


    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now][0] < dist:
            continue
        
        for nxt, nxt_cost in graph[now]:
            cost = dist + nxt_cost
            
            if cost < distance[nxt][0]:
                lst = list(distance[now][1])
                lst.append(nxt)
                distance[nxt] = (cost, tuple(lst))
                heapq.heappush(queue, (cost, nxt))

dijkstra(S)
print(distance[E][0])
print(len(distance[E][1]))
print(*distance[E][1])
