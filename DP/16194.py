# Solved on 2021. 08. 31.
# 16194 카드 구매하기 2

import sys
input = sys.stdin.readline

N = int(input())

d = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, (i+2)//2):
        d[i] = min(d[i], d[j] + d[i-j])

print(d[N])
