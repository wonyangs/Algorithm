# Solved on 2020.12.28
# 3-2 큰 수의 법칙

# ---------------------------

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
first = a[-1]
second = a[-2]
count = m // (k+1)
sum = 0

sum += first * (m - count)
sum += second * count

print(sum)
