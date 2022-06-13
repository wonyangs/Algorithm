# Solved on 2022. 6. 13.
# 2023 신기한 소수

import sys
from math import sqrt
input = sys.stdin.readline

def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def dfs(n, depth):
    if depth >= N:
        if is_prime(n):
            print(n)
        return
    
    for i in range(1, 10):
        if is_prime(n):
            dfs(n * 10 + i, depth+1)

N = int(input())

for i in range(2, 10):
    dfs(i, 1)
