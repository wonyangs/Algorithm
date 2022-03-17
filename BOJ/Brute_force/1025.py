# Solved on 2022. 3. 17.
# 1025 제곱수 찾기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[*map(str, input().strip())] for _ in range(N)]

num_set = set()
for x in range(N):
    for y in range(M):
        for i in range(-N, N):
            for j in range(-M, M):
                arr = []
                nx, ny = x, y
                while 0 <= nx < N and 0 <= ny < M:
                    arr.append(graph[nx][ny])
                    nx, ny = nx + i, ny + j
                    
                    if arr:
                        num_set.add(int(''.join(arr)))
                    if i == 0 and j == 0:
                        break
MAX = -1
for n in num_set:
    if int(n**0.5)**2 == n:
        MAX = max(MAX, n)
print(MAX)
