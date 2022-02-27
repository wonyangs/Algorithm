# Solved on 2022. 2. 27.
# 2559 수열

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [*map(int, input().split())]

hap = sum(arr[:K])
MAX = hap
for i in range(N-K):
    hap -= arr[i]
    hap += arr[K+i]
    MAX = max(MAX, hap)
print(MAX)
