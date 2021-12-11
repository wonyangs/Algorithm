# Solved on 2021. 12. 11.
# 2623 음악프로그램

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
targeted = [0] * (N+1)
for i in range(M):
    for j in range(1, arr[i][0]):
        a, b = arr[i][j], arr[i][j+1]
        graph[a].append(b)
        targeted[b] += 1

queue = deque()
res = []
for i in range(1, N+1):
    if targeted[i] == 0:
        queue.append(i)
while queue:
    now = queue.popleft()
    res.append(now)
    for n in graph[now]:
        targeted[n] -= 1
        if targeted[n] == 0:
            queue.append(n)

if len(res) == N:
    for n in res:
        print(n)
else:
    print(0)
