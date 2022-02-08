# Solved on 2022. 2. 8.
# 14003 가장 긴 증가하는 부분 수열 5

import bisect
import sys
input = sys.stdin.readline


N = int(input())
arr = [*map(int, input().split())]

lis, dp = [arr[0]], [0]
for n in arr[1:]:
    if n > lis[-1]:
        lis.append(n)
        dp.append(len(lis)-1)
    else:
        idx = bisect.bisect_left(lis, n)
        lis[idx] = n
        dp.append(idx)

MAX, count = -1, -1
res = []
for i in range(len(dp)-1, -1, -1):
    if dp[i] > MAX:
        MAX = dp[i]
        count = MAX-1
        res = []
        res.append(arr[i])
    elif count == dp[i]:
        res.append(arr[i])
        count -= 1
print(len(lis))
print(*res[::-1])
