# Solved on 2022. 6. 17.
# 3197 백조의 호수

from collections import deque
import sys
input = sys.stdin.readline


def ice_bfs(first_ice):
    queue = deque()
    visit = [[0] * C for _ in range(R)]
    for x, y in first_ice:
        queue.append((x, y))
        visit[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if not visit[nx][ny] and graph[nx][ny] == 'X':
                queue.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
    return visit


def swan_bfs(ice_graph, coor):
    queue = deque()
    next_queue = deque()
    visit = [[False] * C for _ in range(R)]
    queue.append((coor[0], coor[1]))
    visit[coor[0]][coor[1]] = True

    day = -1
    while True:
        day += 1
        for x, y in next_queue:
            queue.append((x, y))
        next_queue = deque()
        while queue:
            x, y = queue.popleft()
            if x == coor[2] and y == coor[3]:
                return day

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if not visit[nx][ny] and ice_graph[nx][ny] <= day:
                    queue.append((nx, ny))
                    visit[nx][ny] = True
                if not visit[nx][ny] and ice_graph[nx][ny] == day + 1:
                    next_queue.append((nx, ny))
                    visit[nx][ny] = True


R, C = map(int, input().split())
graph = [[*map(str, input().strip())] for _ in range(R)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

swan_coor = [-1, -1, -1, -1]
first_ice = set()

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'L':
            if swan_coor[0] == -1:
                swan_coor[0], swan_coor[1] = i, j
            else:
                swan_coor[2], swan_coor[3] = i, j
            graph[i][j] = '.'

        if graph[i][j] == '.':
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if graph[nx][ny] == 'X':
                    first_ice.add((nx, ny))
print(swan_bfs(ice_bfs(first_ice), swan_coor))


