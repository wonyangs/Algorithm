# Solved on 2021. 09. 28.
# 14891 톱니바퀴

import sys
input = sys.stdin.readline


def moveGear(gear, d):
    # 시계방향으로 기어 회전
    if d == 1:
        tmp1 = gear[0]
        for i in range(7):
            tmp2 = gear[i+1]
            gear[i+1] = tmp1
            tmp1 = tmp2
        gear[0] = tmp1
    # 반시계방향으로 기어 회전
    if d == -1:
        tmp1 = gear[7]
        for i in range(7, 0, -1):
            tmp2 = gear[i-1]
            gear[i-1] = tmp1
            tmp1 = tmp2
        gear[7] = tmp1


def checkGear(n, d):
    gearDirections = [0, 0, 0, 0, 0]
    gearDirections[n] = d

    # 기준 기어 왼쪽 확인
    for i in range(n, 1, -1):
        if gearDirections[i] == 0:
            break

        if gearList[i][6] != gearList[i-1][2]:
            if gearDirections[i] == -1:
                gearDirections[i-1] = 1
            else:
                gearDirections[i-1] = -1

    # 기준 기어 오른쪽 확인
    for i in range(n, 4):
        if gearDirections[i] == 0:
            break

        if gearList[i][2] != gearList[i+1][6]:
            if gearDirections[i] == -1:
                gearDirections[i+1] = 1
            else:
                gearDirections[i+1] = -1

    return gearDirections


# N극은 0, S극은 1
gearA = list(map(int, input().strip()))
gearB = list(map(int, input().strip()))
gearC = list(map(int, input().strip()))
gearD = list(map(int, input().strip()))
gearList = [None, gearA, gearB, gearC, gearD]

K = int(input())

for _ in range(K):
    # direction : 1 시계방향, -1 반시계방향
    gearNum, direction = map(int, input().split())
    d = checkGear(gearNum, direction)
    for i in range(1, 5):
        moveGear(gearList[i], d[i])

hap = 0
if gearList[1][0] == 1:
    hap += 1
if gearList[2][0] == 1:
    hap += 2
if gearList[3][0] == 1:
    hap += 4
if gearList[4][0] == 1:
    hap += 8
print(hap)
