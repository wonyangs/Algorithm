# Solved on 2022. 5. 23.
# 2902 KMP는 왜 KMP일까?

import sys
input = sys.stdin.readline

arr = [*map(str, input().split('-'))]
for i in range(len(arr)):
    print(arr[i][0], end='')
print()
