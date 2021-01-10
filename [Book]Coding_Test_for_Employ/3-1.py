# Solved on 2020.12.28
# 3-1 거스름돈

# ---------------------------

import sys
input = sys.stdin.readline


coin_list = [500, 100, 50, 10]
count = 0

n = int(input())

for coin in coin_list:
    count += n // coin
    n %= coin

print(count)
