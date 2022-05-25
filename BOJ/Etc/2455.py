# Solved on 2022. 5. 26.
# 2455 지능형 기차

import sys
input = sys.stdin.readline

MAX = 0
train = 0

for _ in range(4):
    a, b = map(int, input().split())
    train -= a
    train += b
    MAX = max(MAX, train)
print(MAX)