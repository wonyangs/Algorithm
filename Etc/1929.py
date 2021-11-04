# Solved on 2021. 11. 04.
# 1929 소수 구하기

import sys
input = sys.stdin.readline

M, N = map(int, input().split())

MAX = 0
for i in range(N):
    if i * i > N:
        MAX = i
        break

arr = [1] * (N+1)
primeNum = []
for i in range(2, MAX):
    isPrime = True
    for n in primeNum:
        if i % n == 0:
            isPrime = False
            break
    if isPrime:
        primeNum.append(i)
        k = i + i
        while k <= N:
            arr[k] = 0
            k += i

arr[1] = 0
for i in range(M, N+1):
    if arr[i] == 1:
        print(i)
