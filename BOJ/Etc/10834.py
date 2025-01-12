from collections import deque
from math import gcd

M = int(input())
belts = [tuple(map(int, input().split())) for _ in range(M)]
d, s = [0] * (M + 1), [1] + [0] * M

for i in range(M):
    a, b, x = belts[i]
    s[i+1] = s[i] * b // a
    d[i+1] = d[i] ^ x

print(d[M], s[M])
