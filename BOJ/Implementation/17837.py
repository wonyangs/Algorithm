# Solved on 2022. 2. 6.
# 17837 새로운 게임 2

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
map_info = [[*map(int, input().split())] for _ in range(N)]
graph = [[[] for _ in range(N)] for _ in range(N)]
for i in range(1, K+1):
    x, y, d = map(int, input().split())
    graph[x-1][y-1].append([i, d])

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
time, gameover = 0, False
while time <= 1000 and not gameover:
    time += 1
    for n in range(1, K+1):
        # 움직일 말 좌표 탐색
        for i in range(N):
            for j in range(N):
                for k in range(len(graph[i][j])):
                    if graph[i][j][k][0] == n:
                        x, y, idx = i, j, k
                        piece = graph[i][j][k]
        
        # 다음 칸 정보 조회
        color = -1
        nx, ny = x + dx[piece[1]-1], y + dy[piece[1]-1]
        if 0 <= nx < N and 0 <= ny < N:
            color = map_info[nx][ny]
        
        # 파랑, 장외일 경우 방향 돌려 재탐색
        if color == -1 or color == 2:
            change_dir = [0, 2, 1, 4, 3]
            piece[1] = change_dir[piece[1]]
            nx, ny = x + dx[piece[1]-1], y + dy[piece[1]-1]
            color = -1
            if 0 <= nx < N and 0 <= ny < N:
                color = map_info[nx][ny]
        
        # 흰색, 빨강일 경우에만 이동
        if color == 0 or color == 1:
            to_move_pieces = []
            to_move_pieces = graph[x][y][idx:]
            graph[x][y] = graph[x][y][:idx]
            if color == 1:
                to_move_pieces.reverse()
            graph[nx][ny] += to_move_pieces
    
        #게임종료 확인
        for i in range(N):
            for j in range(N):
                if len(graph[i][j]) >= 4:
                    gameover = True

if time > 1000:
    print(-1)
else:
    print(time)
