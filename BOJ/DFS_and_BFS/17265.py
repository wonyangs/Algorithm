from collections import deque


def min_bfs(N, arr):
    x, y = 0, 0
    dx, dy = [1, 0], [0, 1]
    
    visit = [[1e9] * N for _ in range(N)]
    visit[0][0] = int(arr[x][y])
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        now = visit[x][y]
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if arr[nx][ny] == '+':
                for j in range(2):
                    mx, my = nx + dx[j], ny + dy[j]
                    if mx < 0 or my < 0 or mx >= N or my >= N:
                        continue
                    if visit[mx][my] > now + int(arr[mx][my]):
                        visit[mx][my] = now + int(arr[mx][my])
                        queue.append((mx, my))
                        
            elif arr[nx][ny] == '*':
                for j in range(2):
                    mx, my = nx + dx[j], ny + dy[j]
                    if mx < 0 or my < 0 or mx >= N or my >= N:
                        continue
                    if visit[mx][my] > now * int(arr[mx][my]):
                        visit[mx][my] = now * int(arr[mx][my])
                        queue.append((mx, my))
                        
            elif arr[nx][ny] == '-':
                for j in range(2):
                    mx, my = nx + dx[j], ny + dy[j]
                    if mx < 0 or my < 0 or mx >= N or my >= N:
                        continue
                    if visit[mx][my] > now - int(arr[mx][my]):
                        visit[mx][my] = now - int(arr[mx][my])
                        queue.append((mx, my))
    return visit[-1][-1]


def max_bfs(N, arr):
    x, y = 0, 0
    dx, dy = [1, 0], [0, 1]
    
    visit = [[-1e9] * N for _ in range(N)]
    visit[0][0] = int(arr[x][y])
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        now = visit[x][y]
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if arr[nx][ny] == '+':
                for j in range(2):
                    mx, my = nx + dx[j], ny + dy[j]
                    if mx < 0 or my < 0 or mx >= N or my >= N:
                        continue
                    if visit[mx][my] < now + int(arr[mx][my]):
                        visit[mx][my] = now + int(arr[mx][my])
                        queue.append((mx, my))
                        
            elif arr[nx][ny] == '*':
                for j in range(2):
                    mx, my = nx + dx[j], ny + dy[j]
                    if mx < 0 or my < 0 or mx >= N or my >= N:
                        continue
                    if visit[mx][my] < now * int(arr[mx][my]):
                        visit[mx][my] = now * int(arr[mx][my])
                        queue.append((mx, my))
                        
            elif arr[nx][ny] == '-':
                for j in range(2):
                    mx, my = nx + dx[j], ny + dy[j]
                    if mx < 0 or my < 0 or mx >= N or my >= N:
                        continue
                    if visit[mx][my] < now - int(arr[mx][my]):
                        visit[mx][my] = now - int(arr[mx][my])
                        queue.append((mx, my))
    return visit[-1][-1]
    

N = int(input())
arr = [input().split() for _ in range(N)]
print(max_bfs(N, arr), min_bfs(N, arr))
