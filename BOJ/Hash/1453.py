# Solved on 2022. 7. 2.
# 1453 피시방 알바

import sys
input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]
arr_set = set()
count = 0
for n in arr:
    if n not in arr_set:
        arr_set.add(n)
    else:
        count += 1
print(count)
