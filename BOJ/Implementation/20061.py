# Solved on 2022. 2. 13.
# 20061 모노미노도미노 2

from collections import deque
import sys
input = sys.stdin.readline


def change_matrix(blocks):
    tmp = []
    for x, y in blocks:
        tmp.append((y, x))
    return tmp


def add_block(color, blocks):
    new_blocks = []
    if len(blocks) == 1 or blocks[0][0] == blocks[1][0]:
        for x, y in blocks:
            new_blocks.append((0, y))
    else:
        new_blocks.append((0, blocks[0][1]))
        new_blocks.append((1, blocks[0][1]))
    can_move = True
    max_x = 0
    for i in range(6):
        for x, y in new_blocks:
            if x+i > 5 or color[x+i][y] == 1:
                can_move = False
                break
        if can_move:
            max_x = i
    for x, y in new_blocks:
        color[x+max_x][y] = 1


def set_block(blocks):
    add_block(green, blocks)
    add_block(blue, change_matrix(blocks))


def check_line(color):
    global score
    for i in range(6):
        if 0 not in color[i]:
            del color[i]
            score += 1
            color.appendleft([0, 0, 0, 0])

def check_area(color):
    count = 0
    for i in range(2):
        if 1 in color[i]:
            count += 1
    for i in range(count):
        color.pop()
        color.appendleft([0, 0, 0, 0])

def update(color):
    check_line(color)
    check_area(color)


N = int(input())
green = deque([[0]*4 for _ in range(6)])
blue =  deque([[0]*4 for _ in range(6)])
score = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    if t == 1:
        set_block([(x, y)])
    elif t == 2:
        set_block([(x, y), (x, y+1)])
    elif t == 3:
        set_block([(x, y), (x+1, y)])

    update(green)
    update(blue)
print(score)
hap = 0
for i in range(6):
    hap += sum(green[i])
    hap += sum(blue[i])
print(hap)
