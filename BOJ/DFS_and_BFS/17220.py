# Solved on 2022. 12. 18.
# 17220 마약수사대

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(start, visit):
    queue = deque()
    queue.append(start)
    visit.add(start)
    
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if nxt in visit:
                continue
            queue.append(nxt)
            visit.add(nxt)

N, M = map(int, input().split())
graph = defaultdict(list)
indegree = defaultdict(int)
for _ in range(M):
    a, b = input().split()
    graph[a].append(b)
    indegree[a] += 0
    indegree[b] += 1
info = input().split()

for n in info[1:]:
    graph[n] = []
res = set()
for n in indegree.keys():
    if indegree[n] == 0 and n not in set(info[1:]):
        bfs(n, res)
        res.remove(n)
for n in info[1:]:
    if n in res:
        res.remove(n)
print(len(res))
