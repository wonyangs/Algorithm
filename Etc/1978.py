# Solved on 2020.12.14
# 1978 소수 찾기

import sys

input()

a = map(int, sys.stdin.readline().split())
count = 0
for i in a:
    tmp = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            tmp += 1
    if tmp == 0:
        count += 1

print(count)
