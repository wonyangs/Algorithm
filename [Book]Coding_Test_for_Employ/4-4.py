# Solved on 2020.12.31
# 4-4 게임 개발

# ---------------------------

import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n = 세로크기 m = 가로크기
a, b, d = map(int, input().split())  # a = 북쪽으로부터 거리 b = 서쪽으로부터 거리
play_map = []
count = 1
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서

for _ in range(n):
    play_map.append(list(map(int, input().split())))

while True:
    play_map[a][b] = 2

    for i in range(4):
        direct = (d + 3) % 4
        na = a + direction[direct][0]
        nb = b + direction[direct][1]

        if na < 0 or nb < 0 or na >= n or nb >= m:
            d = direct
            continue

        if play_map[na][nb] == 0:
            a = na
            b = nb
            d = direct
            count += 1
            break
        else:
            d = direct
            if i == 3:
                a -= direction[d][0]
                b -= direction[d][1]

    if play_map[a][b] == 1:
        break

print(count)
