# Solved on 2021. 10. 27.
# 15649 N과 M (1)

from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

com = list(permutations(arr, m))

for i in com:
    for num in i:
        print(num, end=' ')
    print()
