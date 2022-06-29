# Solved on 2022. 6. 30.
# 1063 킹

import sys
input = sys.stdin.readline

def out_of_range(x, y):
    return x < 0 or y < 0 or x >= 8 or y >= 8

def int_to_chr(coor):
    return chr(ord('A') + coor[1]) + str(coor[0] + 1)

coor = {}
for i in range(8):
    coor[chr(ord('A') + i)] = i

move = {"R": (0, 1), "L": (0, -1), "B": (-1, 0), "T": (1, 0),
        "RT": (1, 1), "LT": (1, -1), "RB": (-1, 1), "LB": (-1, -1)}

info_arr = input().strip().split()
king_coor = [int(info_arr[0][1]) - 1, coor[info_arr[0][0]]]
stone_coor = [int(info_arr[1][1]) - 1, coor[info_arr[1][0]]]

for _ in range(int(info_arr[2])):
    cmd = input().strip()
    dx, dy = move[cmd]
    kx, ky = king_coor[0] + dx, king_coor[1] + dy
    if out_of_range(kx, ky):
        continue
    if kx == stone_coor[0] and ky == stone_coor[1]:
        sx, sy = stone_coor[0] + dx, stone_coor[1] + dy
        if out_of_range(sx, sy):
            continue
        stone_coor = [sx, sy]
    king_coor = [kx, ky]

print(int_to_chr(king_coor))
print(int_to_chr(stone_coor))
