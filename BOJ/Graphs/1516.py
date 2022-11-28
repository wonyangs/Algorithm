# Solved on 2022. 11. 28.
# 1005 ACM Craft

import sys
import heapq

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
time = [0] * (N + 1)
for i in range(1, N + 1):
    arr = [*map(int, input().split())]
    time[i] = arr[0]
    
    for n in arr[1:]:
        if n == -1:
            break
        indegree[i] += 1
        graph[n].append(i)

heap = []
visit = set()
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, (time[i], i))
        visit.add(i)

res = [0] * (N + 1)
while heap:
    tm, n = heapq.heappop(heap)
    res[n] = tm
    
    for nxt in graph[n]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0 and nxt not in visit:
            heapq.heappush(heap, (tm + time[nxt], nxt))

print(*res[1:], sep='\n')
