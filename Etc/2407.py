# Solved on 2021. 09. 23.
# 2407 조합

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = 1
for i in range(n, n-m, -1):
    result *= i

result //= math.factorial(m)
print(result)
