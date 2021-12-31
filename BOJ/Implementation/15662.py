# Solved on 2021. 10. 06.
# 15662 톱니바퀴 (2)

from collections import deque
import sys
input = sys.stdin.readline


# 기어 회전
def rotate(arr, d):
    queue = deque(arr)
    queue.rotate(d)
    return list(queue)


def checkGear(num, d):
    move = [0] * (T+1)
    move[num] = d

    # 왼쪽 체크
    for i in range(num, 1, -1):
        if gear[i][6] != gear[i-1][2]:
            if move[i] == 1:
                move[i-1] = -1
            else:
                move[i-1] = 1
        else:
            break
    # 오른쪽 체크
    for i in range(num, T):
        if gear[i][2] != gear[i+1][6]:
            if move[i] == 1:
                move[i+1] = -1
            else:
                move[i+1] = 1
        else:
            break
    return move


T = int(input())
gear = [[]]

for _ in range(T):
    gear.append(list(map(int, input().strip())))

K = int(input())

for _ in range(K):
    num, direction = map(int, input().split())
    arr = checkGear(num, direction)
    for i in range(1, T+1):
        gear[i] = rotate(gear[i], arr[i])

res = 0
for i in range(1, T+1):
    if gear[i][0] == 1:
        res += 1
print(res)
