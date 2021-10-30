# Solved on 2021. 10. 30.
# 4948 베르트랑 공준

import sys
input = sys.stdin.readline

MAX = 123456 * 2 + 1
dp = [1] * MAX

primeNum = []


for i in range(1, MAX):
    if i*i > MAX:
        p = i
        break

for i in range(2, p):
    if dp[i] != 1:
        continue

    prime = True
    for j in primeNum:
        if i % j == 0:
            prime = False
            break
    if prime is True:
        primeNum.append(i)
        k = i + i
        while k < MAX:
            dp[k] = 0
            k += i

while True:
    n = int(input())
    if n == 0:
        break

    print(sum(dp[n+1:2*n+1]))
