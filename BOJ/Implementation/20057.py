# Solved on 2022. 2. 20.
# 20057 마법사 상어와 토네이도

from math import trunc
import sys
input = sys.stdin.readline   

N = int(input())
sand_graph = [[*map(int, input().split())] for _ in range(N)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
tx = [-2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2] 
ty = [0, -1, 0, 1, -2, -1, 1, 2, -1, 0, 1, 0]
sand_move = [[2, 10, 7, 1, 5, -1, 0, 0, 10, 7, 1, 2],
            [0, 1, 0, 1, 2, 7, 7, 2, 10, -1, 10, 5],
            [2, 1, 7, 10, 0, 0, -1, 5, 1, 7, 10, 2],
            [5, 10, -1, 10, 2, 7, 7, 2, 1, 0, 1, 0]]

x, y = (N-1)//2, (N-1)//2
t_dir, t_power = 0, 1
count = 0
res_sand = 0
power_up = False
while True:
    count += 1
    
    # 토네이도 이동
    x, y = x+dx[t_dir], y+dy[t_dir]
    
    # 모래 뿌리기
    left_sand = sand_graph[x][y]
    lx, ly = -1, -1
    for i in range(len(tx)):
        nx, ny = x+tx[i], y+ty[i]
        if sand_move[t_dir][i] == -1:
            lx, ly = nx, ny
            continue
        moving_sand = trunc(sand_graph[x][y] * (sand_move[t_dir][i] * 0.01))
        left_sand -= moving_sand
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            res_sand += moving_sand
        else:
            sand_graph[nx][ny] += moving_sand
    if lx < 0 or ly < 0 or lx >= N or ly >= N:
        res_sand += left_sand
    else:
        sand_graph[lx][ly] += left_sand
    sand_graph[x][y] = 0
    
    # 토네이도 정보 변경
    if count == t_power:
        t_dir = (t_dir+1)%4
        count = 0
        if power_up:
            t_power += 1
            power_up = False
        else:
            power_up = True
    
    
    # 토네이도 소멸
    if x == 0 and y == 0:
        break
print(res_sand)
