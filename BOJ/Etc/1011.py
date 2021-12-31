# Solved on 2021. 10. 15.
# 1011 Fly me to the Alpha Centauri

import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x

    move = 1
    i = 0
    while distance > i:
        i += move * 2
        move += 1
    move -= 1
    if distance <= i - move:
        print(move*2-1)
    else:
        print(move*2)
