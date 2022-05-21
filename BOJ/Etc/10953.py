# Solved on 2022. 5. 21.
# 10953 A+B - 6

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a, b = map(int, input().split(','))
    print(a+b)

