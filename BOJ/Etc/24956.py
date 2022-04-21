# Solved on 2022. 4. 22.
# 24956 나는 정말 휘파람을 못 불어

import sys
input = sys.stdin.readline

N = int(input())
param = input().strip()

w_count, h_count, e_count, res = 0, 0, 0, 0
for c in param:
    if c == 'W':
        w_count += 1
    elif c == 'H':
        h_count += w_count
    elif c == 'E':
        res = (res * 2) % 1000000007
        res += e_count
        e_count += h_count

print(res % 1000000007)
