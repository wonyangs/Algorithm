# Solved on 2021. 11. 13.
# 16236 아기 상어

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    global sharkExp
    global sharkSize
    global res
    queue = deque()
    queue.append((x, y))
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visit = [[-1] * N for _ in range(N)]
    visit[x][y] = 0
    graph[x][y] = 0

    dis = []
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visit[nx][ny] == -1 and graph[nx][ny] <= sharkSize:
                queue.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
                if 0 < graph[nx][ny] < sharkSize:
                    dis.append((visit[nx][ny], nx, ny))

    if dis:
        dis.sort()
        d, a, b = dis[0]
        graph[a][b] = 9
        res += d
        sharkExp += 1
        return True
    else:
        return False


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

sharkSize = 2
sharkExp = 0
res = 0

while True:
    catch = False
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                catch = bfs(i, j)
                break
        if catch:
            break
    if catch is False:
        break
    if sharkExp == sharkSize:
        sharkSize += 1
        sharkExp = 0

print(res)
