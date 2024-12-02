import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
visible = [*map(int, input().split())]
graph = defaultdict(list)
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

MAX = float("inf")

def dijkstra():
    hq = []
    heapq.heappush(hq, (0, 0))

    dist = [MAX if v == 0 else 0 for v in visible]
    dist[-1] = MAX
    
    while hq:
        w, n = heapq.heappop(hq)
        
        if w > dist[n]:
            continue
        
        for nxt, nxt_w in graph[n]:
            if dist[nxt] > w + nxt_w:
                dist[nxt] = w + nxt_w
                heapq.heappush(hq, (w + nxt_w, nxt))
                
        
    return dist[-1] if dist[-1] != MAX else -1

res = dijkstra()
print(res)
