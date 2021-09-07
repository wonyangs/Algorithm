# Solved on 2021. 09. 07.
# 2217 로프

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()

for i in range(n):
    arr[i] = arr[i] * (n-i)

print(max(arr))
