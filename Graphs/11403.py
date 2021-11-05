# Solved on 2021. 11. 05.
# 11403 경로 찾기

import sys
input = sys.stdin.readline

INF = int(1e9)


def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == INF:
                print(0, end=' ')
            else:
                print(1, end=' ')
        print()


N = int(input())

graph = []
for _ in range(N):
    m = list(map(int, input().split()))

    tmp = []
    for num in m:
        if num == 0:
            tmp.append(INF)
        else:
            tmp.append(num)
    graph.append(tmp)

floyd()
