# Solved on 2020.12.30
# 4-3 왕실의 나이트

# ---------------------------

import sys
input = sys.stdin.readline


a = list(input().rstrip())

x = ord(a[0])-ord('a')+1
y = int(a[1])

dx = [1, -1, 1, -1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, 1, -1, 1, -1]

count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    count += 1

print(count)
