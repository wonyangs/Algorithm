# Solved on 2021. 12. 05.
# 2143 두 배열의 합

from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
N = int(input())
arrA = list(map(int, input().split()))
M = int(input())
arrB = list(map(int, input().split()))

dictA = defaultdict(int)
count = 0
for i in range(N):
    for j in range(i, N):
        dictA[sum(arrA[i:j+1])] += 1
for i in range(M):
    for j in range(i, M):
        count += dictA[T - sum(arrB[i:j+1])]
print(count)
