# Solved on 2021. 11. 24.
# 15684 사다리 조작

from itertools import combinations
import sys
input = sys.stdin.readline


def ladderGame(graph):
    res = []
    for i in range(N):
        now = i
        for j in range(H):
            if now - 1 >= 0 and graph[j][now-1] == 1:
                now -= 1
                continue
            if now + 1 < N and graph[j][now] == 1:
                now += 1
                continue
        res.append(now)
    for i in range(N):
        if res[i] != i:
            return False
    return True


N, M, H = map(int, input().split())

graph = [[0] * (N-1) for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
for i in range(H):
    for j in range(N-1):
        if graph[i][j] == 1:
            if j - 1 >= 0 and graph[i][j-1] == 0:
                graph[i][j-1] = -1
            if j + 1 < (N-1) and graph[i][j+1] == 0:
                graph[i][j+1] = -1
canPut = []
res = ladderGame(graph)
if res:
    print(0)
else:
    for i in range(H):
        for j in range(N-1):
            if graph[i][j] == 0:
                canPut.append((i, j))
    for i in range(1, 4):
        coms = list(combinations(canPut, i))
        for j in range(len(coms)):
            arr = []
            err = False
            for k in range(i):
                a, b = coms[j][k]
                arr.append((a, b))
            for k in range(i):
                a, b = arr[k]
                if (a, b+1) in arr or (a, b-1) in arr:
                    err = True
            if err:
                continue
    
            for x, y in arr:
                graph[x][y] = 1
            res = ladderGame(graph)
            for x, y in arr:
                graph[x][y] = 0
            if res:
                break
        if res:
            print(i)
            break
    if not res:
        print(-1)
