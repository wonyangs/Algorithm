# Solved on 2022. 4. 4.
# 11635 소인수분해

import sys
input = sys.stdin.readline

N = int(input())

i = 2
while N > 1:
    if N % i == 0:
        print(i)
        N //= i
    else:
        i += 1
