import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
    
hq = []
dist = [float('inf')] * (N + 1)

heapq.heappush(hq, (0, 1))
while hq:
    w, now = heapq.heappop(hq)
    
    for nxt, nxt_w in graph[now]:
        total_w = w + nxt_w
        if dist[nxt] > total_w:
            dist[nxt] = total_w
            heapq.heappush(hq, (total_w, nxt))

print(dist[-1])
