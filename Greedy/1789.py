# Solved on 2021. 09. 04.
# 1789 수들의 합

import sys
input = sys.stdin.readline

s = int(input())
i = 0
hap = 0

while (1):
    i += 1
    if hap + i == s:
        print(i)
        break
    elif hap + i > s:
        print(i-1)
        break
    hap += i
