# Solved on 2020.12.14
# 10816 숫자 카드 2

import sys
import time
start = time.time()

input = sys.stdin.readline


def binary_search(L, n, low, high):
    mid = (low + high) // 2
    if low > high:
        return 0

    if L[mid] == n:
        return L[low:high+1].count(n)
    elif L[mid] > n:
        return binary_search(L, n, low, mid - 1)
    else:
        return binary_search(L, n, mid + 1, high)


n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = tuple(map(int, input().split()))

for i in b:
    tmp = binary_search(a, i, 0, n-1)
    print(tmp, end=' ')

print("time :", time.time() - start)

