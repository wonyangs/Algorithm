# Solved on 2020.12.13
# 10814 나이순 정렬

import sys
input = sys.stdin.readline

n = int(input())
L = []

for i in range(n):
    a, b = map(int, input().split())
    L.append((a, b))

L = sorted(L, key=lambda x: (x[0], x[1]))
for m, n in L:
    print(m, n)

