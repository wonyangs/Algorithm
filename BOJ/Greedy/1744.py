# Solved on 2022. 7. 25.
# 1744 수 묶기

import sys
input = sys.stdin.readline


def hap(arr):
    res = 0
    for i in range(1, len(arr), 2):
        res += arr[i - 1] * arr[i]
    if len(arr) % 2 == 1:
        res += arr[-1]
    return res


N = int(input())
arr = [int(input()) for _ in range(N)]
plus = sorted([i for i in arr if i > 1], reverse=True)
minus = sorted([i for i in arr if i < 1])
print(hap(plus) + hap(minus) + arr.count(1))
