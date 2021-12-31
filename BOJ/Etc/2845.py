# Solved on 2021. 11. 09.
# 2845 파티가 끝나고 난 뒤

import sys
input = sys.stdin.readline

L, P = map(int, input().split())
nums = map(int, input().split())

for n in nums:
    print(n - L * P, end=' ')
print()
