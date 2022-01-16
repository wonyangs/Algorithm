# Solved on 2022. 1. 16.
# 1072 게임

import sys
input = sys.stdin.readline


def binarysearch():
    start, end = 1, int(1e10)
    change = False
    while start <= end:
        mid = (start+end)//2
        nZ = 100 * (Y+mid)//(X+mid)
        if nZ > Z:
            end = mid - 1
            change = True
        else:
            start = mid + 1
    if change:
        return start
    else:
        return -1


X, Y = map(int, input().split())
Z = 100 * Y//X
print(binarysearch())
