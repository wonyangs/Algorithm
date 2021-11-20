# Solved on 2021. 11. 20.
# 1074 Z

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)


def zFind(n, x, y):
    global num
    if n == 0:
        return
    mid = 2 ** (n-1)
    if r < x + mid and c < y + mid:
        zFind(n-1, x, y)
    elif r < x + mid and c >= y + mid:
        num += mid ** 2
        zFind(n-1, x, y + mid)
    elif r >= x + mid and c < y + mid:
        num += (mid ** 2) * 2
        zFind(n-1, x + mid, y)
    else:
        num += (mid ** 2) * 3
        zFind(n-1, x + mid, y + mid)


N, r, c = map(int, input().split())
num = 0
zFind(N, 0, 0)
print(num)
