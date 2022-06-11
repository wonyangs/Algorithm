# Solved on 2022. 6. 11.
# 9085 더하기

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a = input()
    print(sum(map(int, input().split())))
