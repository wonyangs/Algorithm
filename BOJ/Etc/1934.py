# Solved on 2021. 11. 07.
# 1934 최소공배수

from math import gcd
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(A * B // gcd(A, B))
