# Solved on 2021. 11. 08.
# 10757 큰 수 A+B

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

arrA = []
arrB = []

while A > 0:
    arrA.append(A % 10)
    A //= 10
while B > 0:
    arrB.append(B % 10)
    B //= 10

if len(arrA) > len(arrB):
    L = len(arrA)
else:
    L = len(arrB)

res = [0] * (L+1)
for i in range(L):
    if i > len(arrA) - 1:
        a = 0
    else:
        a = arrA[i]
    if i > len(arrB) - 1:
        b = 0
    else:
        b = arrB[i]

    tmp = a + b + res[i]
    res[i] = tmp % 10
    res[i+1] = tmp // 10

res.reverse()
if res[0] != 0:
    print(res[0], end='')
for n in res[1:]:
    print(n, end='')
print()
