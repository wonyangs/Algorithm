# Solved on 2022. 6. 20.
# 23881 알고리즘 수업 - 선택 정렬 1

import sys
input = sys.stdin.readline


def selection_sort(arr):
    count = 0

    for last in range(N, 0, -1):
        max = 0
        max_idx = 0
        for i in range(last):
            if max < arr[i]:
                max = arr[i]
                max_idx = i
        if max_idx != i:
            arr[max_idx], arr[i] = arr[i], arr[max_idx]
            count += 1
            if count == K:
                print(*sorted([arr[max_idx], arr[i]]))
    if count < K:
        print(-1)


N, K = map(int, input().split())
arr = [*map(int, input().split())]
selection_sort(arr)
