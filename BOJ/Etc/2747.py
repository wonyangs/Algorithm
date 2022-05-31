# Solved on 2022. 5. 31.
# 2747 피보나치 수

import sys
input = sys.stdin.readline

def fibo(n):
    if arr[n] != 0:
        return arr[n]
    if n == 0:
        return (0)
    if n == 1:
        arr[1] = 1
        return (1)
    arr[n] = fibo(n-2) + fibo(n-1)
    return fibo(n-2) + fibo(n-1)

n = int(input())
arr = [0] * 50
print(fibo(n))
