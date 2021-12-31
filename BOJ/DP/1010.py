# Solved on 2021. 11. 07.
# 1010 다리 놓기

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    n = 1
    for i in range(N+1, M+1):
        n *= i
    for i in range(1, M-N+1):
        n //= i
    print(n)
