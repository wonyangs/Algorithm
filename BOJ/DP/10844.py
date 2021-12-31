# Solved on 2021. 08. 31.
# 10844 쉬운 계단 수

import sys
input = sys.stdin.readline

q = 1000000000
N = int(input())

d = [0] * (N+1)
dn = [[0] * 10 for i in range(N+1)]

dn[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
d[1] = sum(dn[1])

for i in range(2, N+1):
    dn[i][0] = dn[i-1][1] % q
    for j in range(1, 9):
        dn[i][j] = (dn[i-1][j-1] + dn[i-1][j+1]) % q
    dn[i][9] = dn[i-1][8] % q

    d[i] = (d[i-1] * 2 - (dn[i-1][0]+dn[i-1][9])) % q

print(d[N])
