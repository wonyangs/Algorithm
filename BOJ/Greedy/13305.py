# Solved on 2021. 09. 09.
# 13305 주유소

import sys
input = sys.stdin.readline

n = int(input())

road = list(map(int, input().split()))
price = list(map(int, input().split()))
hap = 0
minPrice = price[0]

for i in range(n-1):
    if price[i] <= minPrice:
        minPrice = price[i]
    hap += minPrice * road[i]

print(hap)
