import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph.keys():
    graph[i].sort()
    
queue = deque([R])
visit = [0] * (N + 1)
visit[R] = 1
cnt = 2
while queue:
    n = queue.popleft()
    
    for nxt in graph[n]:
        if visit[nxt] == 0:
            visit[nxt] = cnt
            cnt += 1
            queue.append(nxt)

for v in visit[1:]:
    print(v)
