# Solved on 2020.12.17
# 1003 피보나치 함수

# ---------------------------

import sys
input = sys.stdin.readline


def fibonacci(n):
    a = 1
    b = 1
    if n == 2:
        return a, b
    else:
        for _ in range(n-2):
            tmp = a + b
            a = b
            b = tmp
        return a, b


def main():
    n = int(input())

    for _ in range(n):
        num = int(input())
        if num == 0:
            print('1 0')
        elif num == 1:
            print('0 1')
        else:
            a, b = fibonacci(num)
            print(a, b)


main()
