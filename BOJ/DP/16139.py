# Solved on 2022. 6. 12.
# 16139 인간-컴퓨터 상호작용

import sys
input = sys.stdin.readline
from collections import defaultdict
from copy import deepcopy

string = input().strip()
N = int(input())

arr = [0] * 26
prefix = [deepcopy(arr)]

for c in string:
    arr[ord(c) - ord('a')] += 1
    prefix.append(deepcopy(arr))
for _ in range(N):
    c, a, b = map(str, input().split())
    sys.stdout.write(str(prefix[int(b)+1][ord(c)-ord('a')] - prefix[int(a)][ord(c)-ord('a')]) + '\n')
