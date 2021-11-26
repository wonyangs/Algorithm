# Solved on 2021. 11. 26.
# 14890 경사로

import sys
input = sys.stdin.readline


def canGo(arr):
    for i in range(N-1):
        if abs(arr[i] - arr[i+1]) > 1:
            return False
    place = [False] * N
    for i in range(N-1):
        if arr[i] > arr[i+1]:
            for j in range(L):
                if i+1+j >= N:
                    return False
                if arr[i+1] != arr[i+1+j]:
                    return False
                else:
                    if place[i+1+j] is True:
                        return False
                    else:
                        place[i+1+j] = True
    for i in range(N-1, 0, -1):
        if arr[i] > arr[i-1]:
            for j in range(L):
                if i-1-j < 0:
                    return False
                if arr[i-1] != arr[i-1-j]:
                    return False
                else:
                    if place[i-1-j] is True:
                        return False
                    else:
                        place[i-1-j] = True
    return True


N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
res = 0
for i in range(N):
    if canGo(graph[i]):
        res += 1
for j in range(N):
    arr = []
    for i in range(N):
        arr.append(graph[i][j])
    if canGo(arr):
        res += 1
print(res)
