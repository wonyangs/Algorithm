import sys
from collections import defaultdict

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in graph.keys():
    graph[i].sort(reverse=True)

queue = [R]
visit = [0] * (N+1)

cnt = 0
while queue:
    n = queue.pop()
    if visit[n] != 0:
        continue
    cnt += 1
    visit[n] = cnt
    
    for nxt in graph[n]:
        queue.append(nxt)
print('\n'.join(map(str, visit[1:])))
