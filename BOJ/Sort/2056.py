# Solved on 2022. 2. 18.
# 2056 작업

import sys
input = sys.stdin.readline

N = int(input())
time_info = [0] * (N+1)
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    arr = [*map(int, input().split())]
    time_info[i] = arr[0]
    indegree[i] = arr[1]
    for j in range(arr[1]):
        graph[i].append(arr[2+j])

time = 0
queue = []
visit = set()
for n in range(1, N+1):
    if indegree[n] == 0 and n not in visit:
        queue.append(n)
        visit.add(n)

while queue:
    MIN = int(1e9)
    MIN_n = -1
    for n in queue:
        if time_info[n] < MIN:
            MIN = time_info[n]
            MIN_n = n
    
    
    for n in queue:
        time_info[n] -= MIN
    time += MIN
    
    for n in queue:
        if time_info[n] == 0:
            for j in range(1, N+1):
                if n in graph[j]:
                    indegree[j] -= 1
            queue.remove(n)
    
    for n in range(1, N+1):
        if indegree[n] == 0 and n not in visit:
            queue.append(n)
            visit.add(n)
print(time)
    