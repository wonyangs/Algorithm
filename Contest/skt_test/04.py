from collections import deque

def bfs(graph, k):
    N = len(graph)
    M = len(graph[0])
    queue = deque()
    x, y = 0, 0
    queue.append((x, y, k))
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    next_day = [(0, 0)]
    day = -1
    while True:
        day += 1
        visit = [[-1] * M for _ in range(N)]
        for x, y in next_day:
            queue.append((x, y, k))
            visit[x][y] = 0
        next_day = []
        while queue:
            x, y, left = queue.popleft()
            if x == N - 1 and y == M - 1:
                return day

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                
                if graph[nx][ny] != '#' and visit[nx][ny] == -1 and left > 0:
                    queue.append((nx, ny, left-1))
                    if graph[nx][ny] == '.':
                        next_day.append((nx, ny))
                    visit[nx][ny] = day

def solution(grid, k):
    graph = [[*map(str, g)] for g in grid]

    return bfs(graph, k)