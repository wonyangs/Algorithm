# Solved on 2022. 5. 30.
# 10156 과자

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

print(a * b - c if c < a * b else 0)
