# Solved on 2022. 6. 1.
# 2576 홀수

import sys
input = sys.stdin.readline

arr = []
for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        arr.append(n)
if (len(arr)):
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
