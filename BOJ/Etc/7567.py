# Solved on 2022. 5. 24.
# 7567 그릇

import sys
input = sys.stdin.readline

arr = [*map(str, input().strip())]
h = 10
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        h += 5
    else:
        h += 10
print(h)
