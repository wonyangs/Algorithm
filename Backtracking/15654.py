# Solved on 2021. 01. 13.
# 15654 N과 M (5)

from itertools import permutations
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
input_nums = sorted(list(map(int, input().split())))

a = list(permutations(input_nums, m))

for result in a:
    for num in result:
        print(num, end=' ')
    print()
