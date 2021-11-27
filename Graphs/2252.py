# Solved on 2021. 11. 27.
# 2252 줄 세우기

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)
node = [0] * (N+1)
queue = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    node[b] += 1

for i in range(1, N+1):
    if visit[i] is False and node[i] == 0:
        queue.append(i)
        visit[i] = True
Topo = []
while queue:
    now = queue.popleft()
    Topo.append(now)
    isChange = []
    for num in graph[now]:
        node[num] -= 1
        if num not in isChange:
            isChange.append(num)
    for n in isChange:
        if visit[n] is False and node[n] == 0:
            queue.append(n)
            visit[n] = True
for n in Topo:
    print(n, end=' ')
print()
