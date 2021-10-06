# Solved on 2021. 10. 06.
# 3055 탈출

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[x][y] = 0
    lastNum = 0
    arr = moveWater()

    while queue:
        x, y = queue.popleft()
        if lastNum != graph[x][y]:
            lastNum = graph[x][y]
            changeWater(arr)
            arr = moveWater()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.' and (nx, ny) not in arr:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
                if graph[nx][ny] == 'D':
                    print(graph[x][y]+1)
                    return

    print('KAKTUS')
    return


def changeWater(arr):
    for i, j in arr:
        graph[i][j] = '*'


def moveWater():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    arr = set()
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '*':
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        continue
                    t = graph[nx][ny]
                    if t != 'D' and t != 'X' and t != '*':
                        arr.add((nx, ny))
    return arr


R, C = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(list(input().strip()))

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            bfs(i, j)
