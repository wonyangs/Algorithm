# Solved on 2021. 11. 07.
# 1094 막대기

import sys
input = sys.stdin.readline

X = int(input())

s = 64
hap = 0
for i in range(1, 8):
    if X >= s:
        X -= s
        hap += 1
    s //= 2

print(hap)
