# Solved on 2020.12.14
# 2164 카드2

import sys

n = int(sys.stdin.readline())

a = [i + 1 for i in range(n)]

while len(a) > 1:
    for i in range(len(a) - 1, -1, -2):
        del a[i]

print(a[0])
