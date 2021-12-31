# Solved on 2021.01.04
# 2667 단지번호붙이기 ver.DFS

# ---------------------------

import sys
input = sys.stdin.readline


def dfs(board, x, y, visited):
    global count
    if x < 0 or y < 0 or x >= n or y >= n:
        return

    if board[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        count += 1
        dfs(board, x-1, y, visited)
        dfs(board, x, y-1, visited)
        dfs(board, x+1, y, visited)
        dfs(board, x, y+1, visited)


n = int(input())
board = []
visited = [[False] * n for _ in range(n)]
count = 0
num = 0
c = []


for _ in range(n):
    board.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            dfs(board, i, j, visited)
            c.append(count)
            count = 0
            num += 1

print(num)
c.sort()
for i in c:
    print(i)
