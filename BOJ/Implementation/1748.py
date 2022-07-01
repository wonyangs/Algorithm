# Solved on 2022. 7. 1.
# 1748 수 이어 쓰기 1

import sys
input = sys.stdin.readline

N = int(input())
res = 0
for i in range(len(str(N))-1, -1, -1):
    res += N - (10 ** i) + 1
print(res)
