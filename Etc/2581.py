# Solved on 2021. 11. 07.
# 2581 소수

import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

r = 0
for i in range(N):
    if i*i > N:
        r = i
        break

nums = [0] * (N+1)
prime = []
for i in range(2, r):
    isPrime = True
    for n in prime:
        if i % n == 0:
            isPrime = False
            break
    if isPrime:
        prime.append(i)
        k = i * i
        while k < N+1:
            nums[k] = 1
            k += i

prime = []
for i in range(M, N+1):
    if i == 1:
        continue
    if nums[i] == 0:
        prime.append(i)

if prime:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)
