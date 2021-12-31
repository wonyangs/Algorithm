# Solved on 2021. 10. 20.
# 1436 영화감독 숌

import sys
input = sys.stdin.readline

N = int(input())

n = 666
count = 0
while True:
    tmp = str(n)
    if '666' in tmp:
        count += 1
    if count == N:
        print(n)
        break
    n += 1
