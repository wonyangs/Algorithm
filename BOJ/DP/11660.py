# Solved on 2021. 09. 22.
# 11660 구간 합 구하기 5

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (N+1)]
prifix = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N):
    graph.append([0] + list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        hap = 0
        prifix[i][j] = prifix[i][j-1] + prifix[i-1][j] + graph[i][j] - prifix[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    a = prifix[x1-1][y1-1]
    b = prifix[x1-1][y2]
    c = prifix[x2][y1-1]
    d = prifix[x2][y2]

    print(d-b-c+a)
