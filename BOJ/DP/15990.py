# Solved on 2021. 08. 31.
# 15990 1, 2, 3 더하기 5

import sys
input = sys.stdin.readline

T = int(input())
q = 1000000009
n = []

for i in range(T):
    n.append(int(input()))

d = [0, 0, 0] * (max(n)+1)

d[1] = [1, 0, 0]
d[2] = [0, 1, 0]
d[3] = [1, 1, 1]

for i in range(4, max(n)+1):
    d[i] = [(sum(d[i-1])-d[i-1][0]) % q, (sum(d[i-2])-d[i-2][1]) % q, (sum(d[i-3])-d[i-3][2]) % q]

for i in n:
    print(sum(d[i]) % q)
