# Solved on 2021. 11. 03.
# 2947 나무 조각

import sys
input = sys.stdin.readline


def swap(a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

    for n in arr:
        print(n, end=' ')
    print()


arr = list(map(int, input().split()))
end = [1, 2, 3, 4, 5]

while arr != end:
    for i in range(4):
        if arr[i] > arr[i+1]:
            swap(i, i+1)
