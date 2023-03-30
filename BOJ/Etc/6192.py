# Solved on 2023. 03. 30.
# 6182 Roads Around The Farm

from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)


def recf(N):
    if dec[N] != 0:
        return dec[N]
    if (N - K) // 2 <= 0 or (N - K) % 2 != 0:
        dec[N] = 1
        return 1
    dec[N] = recf((N - K) // 2) + recf((N - K) // 2 + K)
    return dec[N]


N, K = map(int, input().split())
dec = defaultdict(int)
print(recf(N))
