# Solved on 2022. 7. 29.
# 9086 문자열

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    str = input().strip()
    print(str[0], str[-1], sep="")
