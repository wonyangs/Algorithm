# Solved on 2021. 01. 12.
# 7576 토마토

from collections import deque
import sys
input = sys.stdin.readline


def print_answer(array):
    max_num = 0
    for i in range(n):
        for num in array[i]:
            if num == 0:
                print(-1)
                return
            elif num > max_num:
                max_num = num
    print(max_num-1)
    return


def BFS(x, y, array):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        v = queue.popleft()
        x = v[0]
        y = v[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            elif array[ny][nx] == 0:
                queue.append((nx, ny))
                array[ny][nx] = array[y][x] + 1


m, n = map(int, input().split())  # m : 가로 n : 세로
array = []
visited = [[False] * m for _ in range(n)]
queue = deque()

for i in range(n):
    array.append(list(map(int, input().split())))
    for j in range(m):
        if array[i][j] == 1:
            queue.append((j, i))


BFS(j, i, array)
print_answer(array)
