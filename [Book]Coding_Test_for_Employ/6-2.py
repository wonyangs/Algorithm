# Solved on 2021.01.08
# 6-2 위에서 아래로

# ---------------------------

import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in range(n):
    print(array[i], end=' ')
