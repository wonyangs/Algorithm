# Solved on 2022. 3. 23.
# 1640 동전 뒤집기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[*map(int, input().strip())] for _ in range(N)]

col_even, col_odd, row_even, row_odd = 0, 0, 0, 0
for g in graph:
    if sum(g) % 2 == 0:
        row_even += 1
    else:
        row_odd += 1

for j in range(M):
    hap = 0
    for i in range(N):
        hap += graph[i][j]
    if hap % 2 == 0:
        col_even += 1
    else:
        col_odd += 1

res1, res2 = 0, 0
res1 += min(col_even, col_odd)
if res1 % 2 == 0:
    res1 += row_odd
else:
    res1 += row_even

res2 += min(row_even, row_odd)
if res2 % 2 == 0:
    res2 += col_odd
else:
    res2 += col_even

print(min(res1, res2))
