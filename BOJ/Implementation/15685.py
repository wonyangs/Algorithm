# Solved on 2021. 10. 06.
# 15685 드래곤 커브

import sys
input = sys.stdin.readline


def generation(arr):
    # 끝 점 좌표
    ex, ey = arr[-1]
    tmp = []

    # 끝 점 (0, 0) 기준으로 평행이동 후 대칭이동
    for i in range(len(arr)-2, -1, -1):
        x, y = arr[i]
        tmp.append((ey-y+ex, x-ex+ey))

    return arr+tmp


N = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dragon = set()

for _ in range(N):
    x, y, d, g = map(int, input().split())
    arr = [(x, y), (x+dx[d], y+dy[d])]
    for _ in range(g):
        arr = generation(arr)
    for n in arr:
        dragon.add(n)

count = 0
dx = [1, 1, 0]
dy = [0, 1, 1]
rect = 0
for x, y in dragon:
    for i in range(3):
        if (x+dx[i], y+dy[i]) in dragon:
            rect += 1
    if rect == 3:
        count += 1
    rect = 0

print(count)
