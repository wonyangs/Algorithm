# Solved on 2021. 12. 26.
# 1780 종이의 개수

import sys
input = sys.stdin.readline

N = int(input())
graph = [[*map(int, input().split())] for _ in range(N)]
count = [0, 0, 0]


def divPaper(x, y, length):
    if length == 1:
        count[graph[x][y]] += 1
        return graph[x][y]
    arr = []
    nxt = length//3
    for i in range(3):
        for j in range(3):
            arr.append(divPaper(x+nxt*i, y+nxt*j, nxt))
    
    if arr[0] == 0:
        for n in arr:
            if n != 0:
                return arr
        count[0] -= 8
        return 0
    elif arr[0] == -1:
        for n in arr:
            if n != -1:
                return arr
        count[-1] -= 8
        return -1
    elif arr[0] == 1:
        for n in arr:
            if n != 1:
                return arr
        count[1] -= 8
        return 1
    else:
        return arr
    

divPaper(0, 0, N)
for i in range(-1, 2):
    print(count[i])
