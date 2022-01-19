# Solved on 2022. 1. 19.
# 15591 MooTube (Silver)

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

def bfs(k, start):
    queue = deque()
    queue.append(start)
    visit = [INF] * (N+1)
    visit[start] -= 1
    
    while queue:
        now = queue.popleft()
        for nxt, val in graph[now]:
            if visit[nxt] != INF:
                continue
            visit[nxt] = min(visit[now], val)
            queue.append(nxt)
    count = 0
    for n in visit[1:]:
        if n >= k:
            count += 1
    print(count-1)


N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
for _ in range(Q):
    k, v = map(int, input().split())
    bfs(k, v)
