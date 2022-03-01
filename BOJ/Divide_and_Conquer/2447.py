# Solved on 2022. 3. 1.
# 2447 별 찍기 - 10

import sys
input = sys.stdin.readline

def star(depth, x, y):
    global graph
    if depth == 0:
        graph[x][y] = '*'
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            nx = x + 3**(depth-1)*i
            ny = y + 3**(depth-1)*j
            star(depth-1, nx, ny)


N = int(input())
cnt = 0
graph = [[' ']*N for _ in range(N)]
while N > 1:
    N //= 3
    cnt += 1
star(cnt, 0, 0)
for g in graph:
    print(''.join(g))