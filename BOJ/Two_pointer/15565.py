# Solved on 2022. 8. 9.
# 15565 귀여운 라이언

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ryan = [i for i, n in enumerate([*map(int, input().split())]) if n == 1]

res = 1000001
for i in range(K - 1, len(ryan)):
    res = min(res, ryan[i] - ryan[i - K + 1])
print(res + 1 if res != 1000001 else -1)
