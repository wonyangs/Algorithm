# Solved on 2021. 01. 09
# 1427 소트인사이드

import sys
input = sys.stdin.readline

n = int(input())
array = []

while n > 0:
    array.append(n % 10)
    n //= 10

array.sort(reverse=True)

for num in array:
    print(num, end='')
