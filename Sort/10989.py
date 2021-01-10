# Solved on 2021. 01. 09
# 10989 수 정렬하기 3

import sys
input = sys.stdin.readline

n = int(input())
array = [0 for _ in range(10001)]

for _ in range(n):
    input_data = int(input())
    array[input_data] += 1


for i in range(10001):
    if array[i] != 0:
        for _ in range(array[i]):
            print(i)
