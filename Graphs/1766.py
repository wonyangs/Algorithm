# Solved on 2021. 11. 27.
# 1766 문제집

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
nodeCount = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    nodeCount[b] += 1

queue = []
Topo = []
for i in range(1, N+1):
    if nodeCount[i] == 0:
        heapq.heappush(queue, i)
while queue:
    now = heapq.heappop(queue)
    Topo.append(now)
    change = []
    for num in graph[now]:
        nodeCount[num] -= 1
        if num not in change:
            change.append(num)
    for num in change:
        if nodeCount[num] == 0:
            heapq.heappush(queue, num)
for n in Topo:
    print(n, end=' ')
print()
