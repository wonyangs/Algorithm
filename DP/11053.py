# Solved on 2021. 09. 01.
# 11053 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

N = int(input())
d = [1] * N

A = list(map(int, input().split()))

for i in range(N-2, -1, -1):
    for j in range(i+1, N):
        if A[j] > A[i]:
            d[i] = max(d[i], d[j]+1)

print(max(d))
