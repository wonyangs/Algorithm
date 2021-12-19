# Solved on 2021. 12. 19.
# 2629 양팔저울

import sys
input = sys.stdin.readline

bwN, bwArr = int(input()), [*map(int, input().split())]
mbN, mbArr = int(input()), [*map(int, input().split())]

MAX = 40000
dp = [0] * (2*MAX+1)
dp[MAX] = 1
for i in bwArr:
    nxt = dp[:]
    for j in range(-MAX, MAX+1):
        if dp[j+MAX] == 0:
            continue
        if j-i >= -MAX:
            nxt[j-i+MAX] = 1
        if j+i <= MAX:
            nxt[j+i+MAX] = 1
    dp = nxt[:]
for n in mbArr:
    if dp[n+MAX]:
        print('Y', end=' ')
    else:
        print('N', end=' ')
print()
