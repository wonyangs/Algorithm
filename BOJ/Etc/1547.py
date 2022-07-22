# Solved on 2022. 7. 22.
# 1547 공

import sys
input = sys.stdin.readline

N = int(input())
arr = [False] * 4
arr[1] = True
for _ in range(N):
    a, b = map(int, input().split())
    if arr[a] or arr[b]:
        arr[a], arr[b] = not arr[a], not arr[b]
print(arr.index(True))
