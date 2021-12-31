# Solved on 2021. 01. 10.
# 18870 좌표 압축

import sys
input = sys.stdin.readline


n = int(input())
array = list(map(int, input().split()))

at = list(sorted(set(array)))
at = {at[i]:i for i in range(len(at))}

for i in array:
    print(at[i], end=' ')
