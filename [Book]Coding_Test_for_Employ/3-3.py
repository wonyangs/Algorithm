# Solved on 2020.12.28
# 3-3 숫자 카드 게임

# ---------------------------

import sys
input = sys.stdin.readline

a = []
n, m = map(int, input().split())

for _ in range(n):
    a.append(min(list(map(int, input().split()))))

print(max(a))
