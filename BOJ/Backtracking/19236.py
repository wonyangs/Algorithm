# Solved on 2022. 2. 14.
# 19236 청소년 상어

from copy import deepcopy as dc
import sys
input = sys.stdin.readline


def shark(base_graph, fx, fy, count, depth):
    global MAX
    
    graph = dc(base_graph)
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == 0:
                shark_x, shark_y, shark_d = i, j, graph[i][j][1]
    
    
    count += graph[fx][fy][0]
    graph[fx][fy][0] = 0
    
    if depth != 0:
        graph[shark_x][shark_y] = [-1, -1]
    
    for n in range(1, 17):
        find = False
        for i in range(4):
            for j in range(4):
                if graph[i][j][0] == n:
                    x, y, d = i, j, graph[i][j][1]
                    find = True
        if not find:
            continue
        for i in range(8):
            nx, ny = x+dx[d], y+dy[d]
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or graph[nx][ny][0] == 0:
                d += 1
                if d == 9: d = 1
                continue
            graph[x][y][1] = d
            tmp = graph[nx][ny]
            graph[nx][ny] = graph[x][y]
            graph[x][y] = tmp
            break
    
    can_move = []
    d = graph[fx][fy][1]
    for i in range(1, 4):
        nx, ny = fx+dx[d]*i, fy+dy[d]*i
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or graph[nx][ny][0] == -1:
            continue
        else:
            can_move.append((nx, ny))
    
    
    if len(can_move):
        for i, j in can_move:
            shark(graph, i, j, count, depth+1)
    else:
        MAX = max(MAX, count)
    
    
graph = [[] for _ in range(4)]
for i in range(4):
    fish = [*map(int, input().split())]
    for j in range(4):
        graph[i].append([fish[2*j], fish[2*j+1]])

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
MAX = 0
shark(graph, 0, 0, 0, 0)
print(MAX)
