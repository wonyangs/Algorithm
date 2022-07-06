# Solved on 2022. 7. 6.
# 1252 이진수 덧셈

import sys
input = sys.stdin.readline

a, b = input().split()
print(bin(int(a, 2) + int(b, 2))[2:])
