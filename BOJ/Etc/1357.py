# Solved on 2022. 5. 20.
# 1357 뒤집힌 덧셈

import sys
input = sys.stdin.readline

a, b = input().split()
print(int(str(int(a[::-1]) + int(b[::-1]))[::-1]))
