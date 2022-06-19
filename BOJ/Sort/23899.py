# Solved on 2022. 6. 19.
# 23899 알고리즘 수업 - 선택 정렬 5

import sys
input = sys.stdin.readline


def selection_sort(arr, tmp):
    if arr == tmp:
        return 1
    for last in range(N, 0, -1):
        max = 0
        max_idx = 0
        for i in range(last):
            if max < arr[i]:
                max = arr[i]
                max_idx = i
        if max_idx != i:
            arr[max_idx], arr[i] = arr[i], arr[max_idx]
        if arr == tmp:
            return 1
    return 0


N = int(input())
arr = [*map(int, input().split())]
tmp = [*map(int, input().split())]
print(selection_sort(arr, tmp))
