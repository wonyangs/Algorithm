# Solved on 2022. 7. 7.
# 1284 집 주소

import sys
input = sys.stdin.readline

while True:
    arr = [*map(int, input().strip())]
    if arr[0] == 0:
        break
    
    res = 0
    for n in arr:
        if n == 1:
            res += 2
        elif n == 0:
            res += 4
        else:
            res += 3
    res += len(arr) + 1
    print(res)
