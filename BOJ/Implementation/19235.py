# Solved on 2022. 2. 16.
# 19235 모노미노도미노

from collections import deque, defaultdict
import sys
input = sys.stdin.readline


def change_matrix(blocks):
    tmp = []
    for x, y in blocks:
        tmp.append((y, x))
    return tmp


def add_block(color, blocks, block_num):
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
            if x+i > 5 or color[x+i][y] != 0:
                can_move = False
                break
        if can_move:
            max_x = i
    for x, y in new_blocks:
        color[x+max_x][y] = block_num


def set_block(blocks):
    global block_num
    add_block(green, blocks, block_num)
    add_block(blue, change_matrix(blocks), block_num)
    block_num += 1


def check_line(color):
    global score
    move = False
    for i in range(6):
        if 0 not in color[i]:
            for j in range(4):
                color[i][j] = 0
            score += 1
            move = True
    if move: down_block(color)
    return move

def down_block(color):
    block_info = defaultdict(list)
    for i in range(6):
        for j in range(4):
            if color[i][j] != 0:
                block_info[color[i][j]].append((i, j))
    for i in range(6):
        for j in range(4):
            color[i][j] = 0
    
    for key, val in sorted(block_info.items()):
        add_block(color, val, key)

def check_area(color):
    count = 0
    for i in range(2):
        if color[i].count(0) != 4:
            count += 1
    for i in range(count):
        color.pop()
        color.appendleft([0, 0, 0, 0])

def update(color):
    while True:
        if not check_line(color):
            break
    check_area(color)


N = int(input())
green = deque([[0]*4 for _ in range(6)])
blue =  deque([[0]*4 for _ in range(6)])
score = 0
block_num = 1
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
    hap += 4-green[i].count(0)
    hap += 4-blue[i].count(0)
print(hap)
