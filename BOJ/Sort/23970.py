# Solved on 2022. 6. 21.
# 23970 알고리즘 수업 - 버블 정렬 3

import sys
input = sys.stdin.readline


def bubble_sort():
    for last in range(N - 1, 0, -1):
        for i in range(last):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                if check_arr[i] == arr[i] and i in diff_idx:
                    diff_idx.remove(i)
                if check_arr[i] != arr[i]:
                    diff_idx.add(i)
                if check_arr[i+1] == arr[i+1] and i+1 in diff_idx:
                    diff_idx.remove(i+1)
                if check_arr[i+1] != arr[i+1]:
                    diff_idx.add(i+1)

                if len(diff_idx) == 0:
                    print(1)
                    sys.exit(0)
    print(0)


N = int(input())
arr = [*map(int, input().split())]
check_arr = [*map(int, input().split())]
diff_idx = set()
for i in range(N):
    if check_arr[i] != arr[i]:
        diff_idx.add(i)
if len(diff_idx) == 0:
    print(1)
    sys.exit(0)
bubble_sort()
