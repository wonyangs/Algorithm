# Solved on 2021. 10. 01.
# 14499 주사위 굴리기

import sys
input = sys.stdin.readline

# n : 세로, m : 가로, x,y : 주사위시작좌표, k : 명령의 개수
n, m, x, y, k = map(int, input().split())

table = []
for i in range(n):
    table.append(list(map(int, input().split())))

command = list(map(int, input().split()))

# 아래, 동, 서, 남, 북, 위
direction = [0, 1, 2, 3, 4, 5]
dice = [0] * 6


def switchDirection(arr):
    tmp = [0] * 6
    for i in range(6):
        tmp[i] = direction[i]

    for i in range(6):
        direction[i] = tmp[arr[i]]


# 명령 실행
for cmd in command:
    if cmd == 1:  # 동쪽으로 이동
        if y + 1 >= m:
            continue

        y += 1
        switchDirection([2, 0, 5, 3, 4, 1])
    elif cmd == 2:  # 서쪽으로 이동
        if y - 1 < 0:
            continue

        y -= 1
        switchDirection([1, 5, 0, 3, 4, 2])
    elif cmd == 3:  # 북쪽으로 이동
        if x - 1 < 0:
            continue

        x -= 1
        switchDirection([3, 1, 2, 5, 0, 4])
    elif cmd == 4:  # 남쪽으로 이동
        if x + 1 >= n:
            continue

        x += 1
        switchDirection([4, 1, 2, 0, 5, 3])
    else:
        continue

    # 복사 진행
    if table[x][y] == 0:
        table[x][y] = dice[direction[0]]
    else:
        dice[direction[0]] = table[x][y]
        table[x][y] = 0

    # 주사위 위쪽 값 출력
    print(dice[direction[5]])
