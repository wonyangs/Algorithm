# Solved on 2021. 08. 30.
# 11052 카드 구매하기

import sys
input = sys.stdin.readline

N = int(input())

d = [0] * (N+1)

P = list(map(int, input().split()))
P.insert(0, 0)

for i in range(1, N+1):
    tmp = []
    for j in range(i):
        tmp.append(P[i-j]+d[j])
    d[i] = max(tmp)

print(d[N])
