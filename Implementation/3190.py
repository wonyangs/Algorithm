# Solved on 2021. 01. 09
# 3190 뱀

from collections import deque
import sys
input = sys.stdin.readline


# 뱀 머리위치 반환
def snakeHead(snakeBody):
    snakeHead = snakeBody[len(snakeBody)-1]
    x = snakeHead[0]
    y = snakeHead[1]

    return x, y


# 게임종료시 False 반환
def isGameOver(snakeBody):
    x, y = snakeHead(snakeBody)
    sb = snakeBody.copy()
    sb.pop()

    if x < 0 or y < 0 or x >= n or y >= n:
        return True

    for nx, ny in sb:
        if nx == x and ny == y:
            return True

    return False


# 머리위치에 사과가 있는지 확인
def isApple(apple, snakeBody):
    x, y = snakeHead(snakeBody)

    for ax, ay in apple:
        if x == ax and y == ay:
            apple.remove((ax, ay))  # 해당 사과 제거
            return True

    return False


# 뱀 움직이기
def moveSnake(snakeBody, direction):
    x, y = snakeHead(snakeBody)  # 현재 머리위치

    if direction == 'up':
        snakeBody.append((x, y-1))
    elif direction == 'down':
        snakeBody.append((x, y+1))
    elif direction == 'left':
        snakeBody.append((x-1, y))
    elif direction == 'right':
        snakeBody.append((x+1, y))
    else:
        print('move Error!')
        return

    if isGameOver(snakeBody):  # 게임 종료 체크
        return

    if not isApple(apple, snakeBody):  # 사과와 닿았는지 체크
        snakeBody.popleft()

    return


# 진행방향 변경
def changeDirection(cmd, direction):
    direct = ['up', 'right', 'down', 'left']
    i = direct.index(direction)

    if cmd == 'D':
        i += 1
        i %= 4
    elif cmd == 'L':
        i -= 1
    else:
        print('cmd Error!')
        return

    return direct[i]


# 정보 입력
n = int(input())  # n = 보드의 크기
k = int(input())  # k = 사과의 개수

apple = []
move = []

for _ in range(k):  # 사과 위치 입력
    input_num = input().split()
    apple.append((int(input_num[1])-1, int(input_num[0])-1))

L = int(input())  # L = 뱀의 방향 변환 횟수

for _ in range(L):  # 뱀 방향 변환 정보 입력
    input_num = input().split()
    move.append((int(input_num[0]), input_num[1]))


# 초기 정보 설정
time = 0  # t = 게임진행시간
direction = 'right'  # 뱀의 진행방향
snakeBody = deque()  # 뱀의 몸이 위치한 좌표

snakeBody.append((0, 0))  # 최초 좌표 추가


# 게임진행
while not isGameOver(snakeBody):
    time += 1
    moveSnake(snakeBody, direction)

    for ctime, cmd in move:
        if time == ctime:
            direction = changeDirection(cmd, direction)


# 게임 종료시간 출력
print(time)
