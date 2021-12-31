# Solved on 2021. 01. 10
# 14503 로봇 청소기

import sys
input = sys.stdin.readline


# 블록 체크
def checkBlock(i, j):
    if array[i][j] == 1:  # 벽
        return 1
    elif array[i][j] == 2:  # 이미 청소
        return 2
    elif array[i][j] == 0:  # 청소안됨
        return 0


# 왼쪽 탐색
def searchLeft():
    global robot, d
    i = robot[0]
    j = robot[1]

    if d == 0:  # North
        return checkBlock(i, j-1)
    elif d == 1:  # East
        return checkBlock(i-1, j)
    elif d == 2:  # South
        return checkBlock(i, j+1)
    elif d == 3:  # West
        return checkBlock(i+1, j)


# 뒤쪽 탐색
def searchBack():
    global robot, d
    i = robot[0]
    j = robot[1]

    if d == 0:  # North
        return checkBlock(i+1, j)
    elif d == 1:  # East
        return checkBlock(i, j-1)
    elif d == 2:  # South
        return checkBlock(i-1, j)
    elif d == 3:  # West
        return checkBlock(i, j+1)


# 주변 청소 확인
def isClean():
    global robot
    i = robot[0]
    j = robot[1]

    if checkBlock(i+1, j) == 2 and checkBlock(i-1, j) == 2 and checkBlock(i, j+1) == 2 and checkBlock(i, j-1) == 2:
        return True
    else:
        return False


# 왼쪽으로 회전
def turnLeft(d):
    return (d-1 + 4) % 4


# 해당 칸 청소
def cleanBlock():
    global robot, count

    if array[robot[0]][robot[1]] != 2:
        array[robot[0]][robot[1]] = 2
        count += 1

    return


# 전진
def goRobot():
    global robot, d
    i = robot[0]
    j = robot[1]

    if d == 0:  # North
        robot = [i-1, j]
    elif d == 1:  # East
        robot = [i, j+1]
    elif d == 2:  # South
        robot = [i+1, j]
    elif d == 3:  # West
        robot = [i, j-1]
    return


# 후진
def backRobot():
    global robot, d
    i = robot[0]
    j = robot[1]

    if d == 0:  # North
        robot = [i+1, j]
    elif d == 1:  # East
        robot = [i, j-1]
    elif d == 2:  # South
        robot = [i-1, j]
    elif d == 3:  # West
        robot = [i, j+1]
    return


# 주변 탐색
def searchMap():
    global robot, d

    for i in range(4):
        result = searchLeft()

        if result == 0:
            d = turnLeft(d)
            goRobot()
            return True
        else:
            d = turnLeft(d)
            continue

    if searchBack() == 1:
        return False
    else:
        backRobot()
        return True


# 정보 입력
n, m = map(int, input().split())  # n : 세로 크기 m : 가로 크기
r, c, d = map(int, input().split())  # r : 북쪽으로부터 칸수 c : 서쪽 d : 방향

array = []
robot = [r, c]  # 초기좌표
canClean = True
count = 0

for _ in range(n):
    array.append(list(map(int, input().split())))


# 청소 시작
while canClean:
    cleanBlock()
    canClean = searchMap()

print(count)
