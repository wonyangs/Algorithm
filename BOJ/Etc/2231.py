# Solved on 2021.01.04
# 2231 분해합

# ---------------------------

import sys
input = sys.stdin.readline


n = int(input())
a = n
L = []


def sum_of_num(num):
    hap = 0

    while num > 0:
        hap += num % 10
        num //= 10

    return hap


while a > 0:
    a -= 1
    if n == a + sum_of_num(a):
        L.append(a)

if len(L) == 0:
    print(0)
else:
    print(min(L))
