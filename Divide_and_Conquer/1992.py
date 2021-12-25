# Solved on 2021. 12. 25.
# 1992 쿼드트리

import sys
input = sys.stdin.readline

N = int(input())
graph = [[*map(int, input().strip())] for _ in range(N)]


def quadTree(x, y, length):
    if length == 1:
        return graph[x][y]
    arr = []
    nxt = length//2
    arr.append(quadTree(x, y, nxt))
    arr.append(quadTree(x, y+nxt, nxt))
    arr.append(quadTree(x+nxt, y, nxt))
    arr.append(quadTree(x+nxt, y+nxt, nxt))
    res = '(' + ''.join([*map(str, arr)]) + ')'
    if arr[0] == 0:
        for i in range(1, 4):
            if arr[i] != 0:
                return res
        return 0
    elif arr[0] == 1:
        for i in range(1, 4):
            if arr[i] != 1:
                return res
        return 1
    else:
        return res


print(quadTree(0, 0, N))
