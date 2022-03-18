# Solved on 2022. 3. 18.
# 16920 확장 게임

from collections import deque
import sys
input = sys.stdin.readline

def m_bfs(x, y, n, n_set):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 0

    for _ in range(player[n]):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if graph[nx][ny] == '.' and visit[nx][ny] > visit[x][y] + 1:
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx, ny))
                    n_set.add((nx, ny))
        if not queue:
            return

def bfs(n):
    n_set = set()

    for x, y in castle[n]:
        m_bfs(x, y, n, n_set)

    castle[n] = n_set
    if len(castle[n]) == 0:
        return False
    
    for x, y in castle[n]:
        graph[x][y] = str(n)
    res[n] += len(castle[n])
    return True

N, M, P = map(int, input().split())
player = [0] + [*map(int, input().split())]
graph = [[*map(str, input().strip())] for _ in range(N)]
castle = [set() for _ in range(P+1)]
visit = [[float('INF')] * M for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
res = [0] * (P+1)
can_play = [False] + [True] * P

for i in range(N):
    for j in range(M):
        if graph[i][j] != '.' and graph[i][j] != '#':
            castle[int(graph[i][j])].add((i, j))
            res[int(graph[i][j])] += 1

while True in can_play:
    for n in range(1, P+1):
        if can_play[n]:
            can_play[n] = bfs(n)
print(*res[1:])
