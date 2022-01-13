# Solved on 2022. 1. 13.
# 10815 숫자 카드

import sys
input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]
card = set()
for n in arr:
    card.add(n)
M = int(input())
checkNum = [*map(int, input().split())]

res = []
for n in checkNum:
    if n in card:
        print(1, end=' ')
    else:
        print(0, end=' ')
print()
