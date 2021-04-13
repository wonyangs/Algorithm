# Solved on 2021. 04. 13.
# 4153 직각삼각형

import sys
input = sys.stdin.readline

while True:
    a = list(map(int, input().split()))
    a.sort()

    if a[2] == 0:
        break

    if a[0]*a[0] + a[1]*a[1] == a[2]*a[2]:
        print("right")
    else:
        print("wrong")
