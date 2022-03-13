# Solved on 2022. 3. 13.
# 6549 히스토그램에서 가장 큰 직사각형

import sys
input = sys.stdin.readline

while True:
    arr = [*map(int, input().split())]
    if arr[0] == 0:
        break

    stack = []
    rec = 0
    for n, h in enumerate(arr[1:]):
        while stack and stack[-1][1] > h:
            tmp = stack.pop()
            if stack:
                rec = max(rec, (n-stack[-1][0]-1)*tmp[1])
            else:
                rec = max(rec, n*tmp[1])
        stack.append((n, h))
    
    while stack:
        tmp = stack.pop()
        if stack:
            rec = max(rec, (arr[0]-stack[-1][0]-1)*tmp[1])
        else:
            rec = max(rec, arr[0]*tmp[1])
    print(rec)
