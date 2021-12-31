# Solved on 2021. 09. 18.
# 1629 곱셈

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

array = []

while b > 1:
    array.append(b % 2)
    b //= 2

array.reverse()

result = a
for i in array:
    result **= 2
    if i == 1:
        result *= a
    result %= c

print(result % c)
