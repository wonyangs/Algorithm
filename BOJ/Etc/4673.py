# Solved on 2021. 10. 16.
# 4673 셀프 넘버

import sys
input = sys.stdin.readline

arr = [False] * 10001

for i in range(1, 10001):
    tmp = [int(i) for i in str(i)]
    n = i + sum(tmp)
    if n < 10001:
        arr[n] = True

for i in range(1, 10001):
    if arr[i] is False:
        print(i)
