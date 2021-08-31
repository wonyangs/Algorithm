# Solved on 2021. 08. 31.
# 14002 가장 긴 증가하는 부분 수열 4

import sys
input = sys.stdin.readline

N = int(input())
d = [1] * N

A = list(map(int, input().split()))

for i in range(N-2, -1, -1):
    for j in range(i+1, N):
        if d[j] >= d[i] and A[j] > A[i]:
            d[i] = max(d[i], d[j]+1)

print(max(d))

maxNum = max(d)
tmp = []

for i in range(N):
    if d[i] == maxNum:
        tmp.append(A[i])
        maxNum -= 1

for i in tmp:
    print(i, end=" ")
