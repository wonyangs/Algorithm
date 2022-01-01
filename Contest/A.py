# Solved on 2021. 12. 31.
# A번 - 2021은 무엇이 특별할까?

import math
import sys
input = sys.stdin.readline

N = int(input())
if N < 4:
    print(6)
else:
    sq = int(math.sqrt(N)) + 1
    prime = []
    nums = [0] * (N+1)
    for n in range(2, sq):
        isPrime = True
        for p in prime:
            if n % p == 0:
                isPrime = False
        if isPrime:
            prime.append(n)
            tmp = n + n
            while tmp <= N:
                nums[tmp] = 1
                tmp += n
    prime = []
    for i in range(2, N):
        if nums[i] == 0:
            prime.append(i)
    
    for i in range(len(prime)):
        if prime[i] * prime[i+1] > N:
            print(prime[i] * prime[i+1])
            break
