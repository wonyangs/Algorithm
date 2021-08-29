# Solved on 2021. 08. 30.
# 15988 1, 2, 3 더하기 3

import sys
input = sys.stdin.readline

T = int(input())
arr = []

for i in range(T):
    arr.append(int(input()))

d = [0] * (max(arr)+3)
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, max(arr)+1):
    d[i] = (d[i-1] + d[i-2] + d[i-3]) % 1000000009

for i in arr:
    print(d[i])
