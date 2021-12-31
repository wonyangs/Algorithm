# Solved on 2021. 08. 30.
# 11727 2xn 타일링 2

import sys
input = sys.stdin.readline

n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-2] * 2 + d[i-1]) % 10007

print(d[n])
