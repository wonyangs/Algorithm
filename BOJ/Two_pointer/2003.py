from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [*map(int, input().split())]

if N != 1:
    psum = [0]
    for n in arr:
        psum.append(psum[-1] + n)
    
    cnt = 0
    i, j = 0, 1
    while i <= N and j <= N:
        if psum[j] - psum[i] == M:
            cnt += 1
            j += 1
        elif psum[j] - psum[i] > M:
            i += 1
        else:
            j += 1

    print(cnt)
else:
    print(1 if arr[0] == M else 0)
