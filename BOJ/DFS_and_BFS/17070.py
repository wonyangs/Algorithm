import sys

input = sys.stdin.readline

N = int(input())
graph = [[*map(int, input().split())] for _ in range(N)]
if graph[N-1][N-1] == 1:
    print(0)
    sys.exit(0)

queue = []

move = [[(0, 1, 0, 1, 0), (0, 1, 1, 1, 2)],
        [(1, 0, 1, 0, 1), (1, 0, 1, 1, 2)],
        [(1, 1, 0, 1, 0), (1, 1, 1, 0, 1), (1, 1, 1, 1, 2)]]

# 0: 가로, 1: 세로, 2: 대각
queue = [(0, 0, 0, 1, 0)]

res = 0
while queue:
    ax, ay, bx, by, t = queue.pop()
    if bx == N - 1 and by == N - 1:
        res += 1
        continue
    
    for adx, ady, bdx, bdy, nt in move[t]:
        anx, any, bnx, bny = ax + adx, ay + ady, bx + bdx, by + bdy
        if anx < 0 or any < 0 or anx >= N or anx >= N or bnx < 0 or bny < 0 or bnx >= N or bny >= N:
            continue
        if graph[anx][any] == 1 or graph[bnx][bny] == 1:
            continue
        if nt == 2 and (graph[anx + 1][any] == 1 or graph[anx][any + 1]):
            continue
        queue.append((anx, any, bnx, bny, nt))
print(res)
