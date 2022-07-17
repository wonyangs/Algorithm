# Solved on 2022. 7. 17.
# 1309 동물원

import sys
input = sys.stdin.readline

N = int(input())
a, b = 1, 2
for _ in range(N - 1):
    a, b = a + b, a * 2 + b
print((a + b) % 9901)
