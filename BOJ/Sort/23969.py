# Solved on 2022. 6. 21.
# 23969 알고리즘 수업 - 버블 정렬 2

import sys
input = sys.stdin.readline


def bubble_sort(arr):
    count = 0
    for last in range(N - 1, 0, -1):
        for i in range(last):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
                if count == K:
                    print(*arr)
                    sys.exit(0)
    print(-1)


N, K = map(int, input().split())
arr = [*map(int, input().split())]
bubble_sort(arr)
