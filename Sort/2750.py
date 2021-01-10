# Solved on 2021.01.09.
# 2750 수 정렬하기

# ---------------------------

import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

for i in range(n):
    print(array[i])
