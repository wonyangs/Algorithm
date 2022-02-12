# Solved on 2022. 2. 12.
# 1052 물병

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
count = 0
while bin(N+count).count('1') > K:
    count +=2 ** bin(N+count)[::-1].index('1')
print(count)
