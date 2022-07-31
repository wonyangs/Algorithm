# Solved on 2022. 7. 31.
# 16401 과자 나눠주기

import sys
input = sys.stdin.readline


def bsearch():
    low, high = 1, max(arr)
    res = 0

    while low <= high:
        mid = (low + high) // 2
        cnt = sum(n // mid for n in arr)

        if cnt >= M:
            low = mid + 1
            res = max(res, mid)
        else:
            high = mid - 1
    return res


M, N = map(int, input().split())
arr = [*map(int, input().split())]
print(bsearch())
