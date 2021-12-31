# Solved on 2021. 08. 30.
# 11052 카드 구매하기

import sys
input = sys.stdin.readline

N = int(input())

d = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, (i+2)//2):
        d[i] = max(d[i], d[j] + d[i-j])

print(d[N])
