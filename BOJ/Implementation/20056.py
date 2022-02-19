# Solved on 2022. 2. 19.
# 20056 마법사 상어와 파이어볼

import sys
input = sys.stdin.readline

def check_dirs(arr):
    for i in range(1, len(arr)):
        if arr[i] % 2 != arr[0] % 2:
            return False
    return True

def move_ball():
    global graph
    # 파이어볼 이동
    new_graph = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for ball in graph[i][j]:
                m, s, d = ball
                nx, ny = (i+dx[d]*s)%N, (j+dy[d]*s)%N
                new_graph[nx][ny].append((m, s, d))
    # 파이어볼 합체
    ball_info = []
    for i in range(N):
        for j in range(N):
            if len(new_graph[i][j]) > 1:
                m_sum, s_sum, dirs = 0, 0, []
                for ball in new_graph[i][j]:
                    m, s, d = ball
                    m_sum += m
                    s_sum += s
                    dirs.append(d)
                ball_info.append((i, j, m_sum//5, s_sum//len(new_graph[i][j]), check_dirs(dirs)))
                new_graph[i][j] = []
    # 파이어볼 분리
    for info in ball_info:
        x, y, m, s, d = info
        if m == 0:
            continue
        if d:
            for i in range(0, 7, 2):
                new_graph[x][y].append((m, s, i))
        else:
            for i in range(1, 8, 2):
                new_graph[x][y].append((m, s, i))
    graph = new_graph

N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append((m, s, d))

for _ in range(K):
    move_ball()

res = 0
for i in range(N):
    for j in range(N):
        for ball in graph[i][j]:
            res += ball[0]
print(res)
