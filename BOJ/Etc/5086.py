# Solved on 2021. 12. 31.
# 5086 배수와 약수

import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")
    