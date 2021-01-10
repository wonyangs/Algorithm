# Solved on 2020.12.13
# 1920 수 찾기

import sys
input = sys.stdin.readline


def Binary_Search(L, N, low, high):
    if low > high:
        return False
    mid = (low + high) // 2

    if N > L[mid]:
        return Binary_Search(L, N, mid + 1, high)
    elif N < L[mid]:
        return Binary_Search(L, N, low, mid - 1)
    else:
        return True


n = int(input())
A = sorted(list(map(int, input().split())))
m = input()
B = list(map(int, input().split()))

for i in B:
    if Binary_Search(A, i, 0, n-1):
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')
