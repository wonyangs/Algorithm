import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split())

dist = [float('inf')] * (N + 1)
hq = []

heapq.heappush(hq, (0, s))
while hq:
    w, now = heapq.heappop(hq)
    
    for nxt, nxt_w in graph[now]:
        total_w = nxt_w + w
        if dist[nxt] > total_w:
            dist[nxt] = total_w
            heapq.heappush(hq, (total_w, nxt))
    
print(dist[t])
