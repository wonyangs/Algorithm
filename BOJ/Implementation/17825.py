# Solved on 2022. 1. 26.
# 17825 주사위 윷놀이

import copy
import sys
input = sys.stdin.readline


def isDice(n, dice):
    for i in dice:
        if i == n:
            return True
        for pool in same_num:
            if n in pool and i in pool:
                return True
    return False


def sol(depth, point, post_dice):
    global MAX
    if depth == 10:
        MAX = max(point, MAX)
        return
    
    # 이번 턴에 움직일 칸 수
    move = dice_moves[depth]
    
    for i in range(4):
        get_point = 0
        dice = copy.deepcopy(post_dice)
        
        for j in range(3):
            if dice[i] == info[j][0]:
                dice[i] = info[j][1]
                break
        
        if dice[i] == -1 or isDice(dice[i]+move, dice):
            continue
        
        dice_in_route = False
        for j in range(3):
            if info[j][1] <= dice[i] <= info[j][2]:
                dice_in_route = True
                if dice[i] + move <= info[j][2]:
                    dice[i] += move
                    get_point = points[dice[i]]
                else:
                    dice[i] = -1
                break
        if not dice_in_route:
            if dice[i] + move <= 20:
                dice[i] += move
                get_point = points[dice[i]]
            else:
                dice[i] = -1
        
        
        dice.sort()
        log_check = []
        log_check.append(point+get_point)
        log_check += dice
        if tuple(log_check) not in log:
            log.add(tuple(log_check))
            sol(depth+1, point+get_point, dice)


dice_moves = [*map(int, input().split())]
points = [0] + [i for i in range(2, 41, 2)] + [10, 13, 16, 19, 25, 30, 35, 40] + [20, 22, 24, 25, 30, 35, 40] + [30, 28, 27, 26, 25, 30, 35, 40]
info = [[5, 21, 28], [10, 29, 35], [15, 36, 43]]
same_num = [[5, 21], [10, 29], [15, 36], [25, 32, 40], [26, 33, 41], [27, 34, 42], [28, 35, 43, 20]]
log = set()
MAX = -1

sol(0, 0, [0, 0, 0, 0])
print(MAX)
