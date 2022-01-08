# Solved on 2022. 1. 8.
# 1389 케빈 베이컨의 6단계 법칙

import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

dist = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    dist[A][B] = 1
    dist[B][A] = 1
for i in range(1, N+1):
    dist[i][i] = 0

for n in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][j] > dist[i][n] + dist[n][j]:
                dist[i][j] = dist[i][n] + dist[n][j]
MIN = INF
res = 0
for n in range(1, N+1):
    if MIN > sum(dist[n][1:]):
        MIN = sum(dist[n][1:]) 
        res = n
print(res)
