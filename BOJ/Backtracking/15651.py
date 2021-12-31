# Solved on 2021. 12. 20.
# 15651 N과 M (3)

import sys
input = sys.stdin.readline


def back(arr, depth):
    if depth >= M:
        for n in arr:
            print(n, end=' ')
        print()
        return
    for i in range(1, N+1):
        arr.append(i)
        back(arr, depth+1)
        arr.pop()


N, M = map(int, input().split())
back([], 0)
