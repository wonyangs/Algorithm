# Solved on 2021. 01. 09
# 11651 좌표 정렬하기 2

import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    input_num = input().split()
    array.append((int(input_num[0]), int(input_num[1])))

array.sort()
array.sort(key=lambda number: number[1])

for a, b in array:
    print(a, b)
