# Solved on 2022. 2. 15.
# 19237 어른 상어

import sys
input = sys.stdin.readline


def is_in_graph(x, y):
    return 0<=x<N and 0<=y<N

def find_shark(num):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == num:
                return [i, j]
    return [-1, -1]

def add_smell():
    for n in range(1, M+1):
        x, y = find_shark(n)
        if x == -1: continue
        smell[x][y] = [n, K]

def remove_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j] != [0, 0]:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j][0] = 0

def game_over():
    hap = 0
    for n in graph:
        hap += sum(n)
    return hap == 1

def move_shark():
    global graph
    for n in range(1, M+1):
        x, y = find_shark(n)
        if x == -1: continue
        move = False
        for d in dist_info[n-1][shark_dist[n-1]-1]:
            nx, ny = x+dx[d-1], y+dy[d-1]
            if is_in_graph(nx, ny) and smell[nx][ny] == [0, 0]:
                move = True
                shark_dist[n-1] = d
                if graph[nx][ny] == 0 or graph[nx][ny] > n:
                    graph[nx][ny] = n
                graph[x][y] = 0
                break
        if move: continue
        for d in dist_info[n-1][shark_dist[n-1]-1]:
            nx, ny = x+dx[d-1], y+dy[d-1]
            if is_in_graph(nx, ny) and smell[nx][ny][0] == n:
                shark_dist[n-1] = d
                if graph[nx][ny] == 0 or graph[nx][ny] > n:
                    graph[nx][ny] = n
                graph[x][y] = 0
                break
        

N, M, K = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
shark_dist = [*map(int, input().split())]
dist_info = [[[*map(int, input().split())] for _ in range(4)] for _ in range(M)]
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

time = 0
add_smell()
while time <= 1000:
    if game_over():
        print(time)
        sys.exit(0)
    time += 1
    move_shark()
    remove_smell()
    add_smell()
print(-1)
