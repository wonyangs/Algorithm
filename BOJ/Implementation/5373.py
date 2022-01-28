# Solved on 2022. 1. 28.
# 5373 큐빙

from collections import deque
import sys
input = sys.stdin.readline


def init_cube():
    color = ['w', 'y', 'r', 'o', 'g', 'b']
    return [[[c]*3 for _ in range(3)] for c in color]


def spin(cube, face, drc):
    face_spin(cube, drc)
    side_spin(cube, face, side_spin_arr(face), drc)


def face_spin(cube, drc):
    cb = ['U', 'D', 'F', 'B', 'L', 'R']
    fc = cube[cb.index(face)]
    if drc == 1:
        fst = [fc[2][0], fc[1][0], fc[0][0]]
        sec = [fc[2][1], fc[1][1], fc[0][1]]
        trd = [fc[2][2], fc[1][2], fc[0][2]]
    elif drc == -1:
        fst = [fc[0][2], fc[1][2], fc[2][2]]
        sec = [fc[0][1], fc[1][1], fc[2][1]]
        trd = [fc[0][0], fc[1][0], fc[2][0]]
    cube[cb.index(face)] = [fst, sec, trd]


def side_spin_arr(face):
    if face == 'U':
        return [('F', 0), ('L', 0), ('B', 0), ('R', 0)]
    elif face == 'D':
        return [('F', 2), ('R', 2), ('B', 2), ('L', 2)]
    elif face == 'F':
        return [('U', 2), ('R', 1), ('D', 0), ('L', 3)]
    elif face == 'B':
        return [('U', 0), ('L', 1), ('D', 2), ('R', 3)]
    elif face == 'L':
        return [('U', 1), ('F', 1), ('D', 1), ('B', 3)]
    elif face == 'R':
        return [('F', 3), ('U', 3), ('B', 1), ('D', 3)]


def side_spin(cube, face, arr, clk):
    tmp = deque()
    for fc, drc in arr:
        tmp.append(get_arr(cube, fc, drc))
    tmp = arr_correction(tmp, face)
    tmp.rotate(clk)
    tmp = arr_correction(tmp, face)
    for i in range(4):
        set_arr(cube, arr[i][0], arr[i][1], tmp[i])


def arr_correction(arr, face):
    if face == "F":
        arr[2].reverse()
        arr[3].reverse()
    elif face == "B":
        arr[1].reverse()
        arr[2].reverse()
    elif face == "L":
        arr[3].reverse()
    elif face == "R":
        arr[2].reverse()
    
    return arr


def get_arr(cube, face, drc):
    cb = ['U', 'D', 'F', 'B', 'L', 'R']
    fc = cube[cb.index(face)]
    if drc == 0:
        return [fc[0][0], fc[0][1], fc[0][2]]
    elif drc == 2:
        return [fc[2][0], fc[2][1], fc[2][2]]
    elif drc == 1:
        return [fc[0][0], fc[1][0], fc[2][0]]
    elif drc == 3:
        return [fc[0][2], fc[1][2], fc[2][2]]


def set_arr(cube, face, drc, arr):
    cb = ['U', 'D', 'F', 'B', 'L', 'R']
    fc = cube[cb.index(face)]
    if drc == 0:
        fc[0][0], fc[0][1], fc[0][2] = arr
    elif drc == 2:
        fc[2][0], fc[2][1], fc[2][2] = arr
    elif drc == 1:
        fc[0][0], fc[1][0], fc[2][0] = arr
    elif drc == 3:
        fc[0][2], fc[1][2], fc[2][2] = arr


def print_upside(cube):
    arr = cube[0]
    for i in range(3):
        for j in range(3):
            print(arr[i][j], end='')
        print()


T = int(input())
for _ in range(T):
    n = int(input())
    direction = [*map(str, input().split())]
    cube = init_cube()
    
    for d in direction:
        face, dct = d[0], d[1]
        if dct == '+':
            spin(cube, face, 1)
        elif dct == '-':
            spin(cube, face, -1)
    print_upside(cube)
