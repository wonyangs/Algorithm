# Solved on 2020.12.29
# 4-1 상하좌우

# ---------------------------

import sys
input = sys.stdin.readline

x, y = 1, 1

n = int(input())
order = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for direction in order:
    for i in range(len(move_types)):
        if move_types[i] == direction:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x = nx
    y = ny

print(x, y)
