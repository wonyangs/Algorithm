# Solved on 2021. 11. 08.
# 2914 저작권

import math
import sys
input = sys.stdin.readline

A, L = map(int, input().split())

res = 0
i = 1
while math.floor(res) < L-1:
    res = i / A
    i += 1
print(i)
