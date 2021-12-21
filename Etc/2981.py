# Solved on 2021. 12. 21.
# 2981 검문

import math
import sys
input = sys.stdin.readline

def divisor(n):
    res = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            res.append(i)
            if n // i not in res:
                res.append(n // i)
    res.sort()
    res = res[1:]
    for n in res:
        print(n, end=' ')
    print()

N = int(input())

arr = [int(input()) for _ in range(N)]
arr.sort()
arr = arr[::-1]
gap = []
for i in range(len(arr)-1):
    gap.append(arr[i]-arr[i+1])

res = gap[0]
for n in gap[1:]:
    res = math.gcd(res, n)
divisor(res)
