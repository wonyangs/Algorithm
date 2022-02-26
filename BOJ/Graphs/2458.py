# Solved on 2022. 2. 26.
# 2458 키 순서

import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
distance = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    distance[a][b] = 1

for i in range(1, N+1):
    distance[i][i] = 0

for n in range(1, N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if distance[i][j] > distance[i][n] + distance[n][j]:
                distance[i][j] = distance[i][n] + distance[n][j]

info = [set() for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if distance[i][j] < INF:
            info[i].add(j)
            info[j].add(i)

res = 0
for s in info:
    if len(s) == N:
        res += 1
print(res)
