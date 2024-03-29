# Solved on 2021. 12. 01.
# 1644 소수의 연속합

import sys
input = sys.stdin.readline


N = int(input())

sqNum = 0
for i in range(1, N):
    if i ** 2 > N:
        sqNum = i
        break

prime = []
nums = [True] * (N+1)
for i in range(2, sqNum):
    isPrime = True
    for n in prime:
        if i % n == 0:
            isPrime = False
    if isPrime:
        prime.append(i)
        k = i * 2
        while k < N+1:
            nums[k] = False
            k += i
primeNum = []
for i in range(2, N+1):
    if nums[i]:
        primeNum.append(i)

if primeNum:
    prefixNums = [primeNum[0]]
else:
    prefixNums = []
for i in range(1, len(primeNum)):
    prefixNums.append(prefixNums[-1] + primeNum[i])
start, end, count = 0, 0, 0
while end < len(prefixNums):
    if prefixNums[end] == N or prefixNums[end] - prefixNums[start] == N:
        count += 1
    if prefixNums[end] - prefixNums[start] < N:
        end += 1
    else:
        start += 1
print(count)
