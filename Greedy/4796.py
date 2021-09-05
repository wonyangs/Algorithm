# Solved on 2021. 09. 05.
# 4796 캠핑

import sys
input = sys.stdin.readline

case = []
count = 0

while(1):
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    useDay = (V // P) * L
    if V % P >= L:
        useDay += L
    else:
        useDay += V % P

    count += 1
    print("Case ", end='')
    print(count, end='')
    print(": ", end='')
    print(useDay)
