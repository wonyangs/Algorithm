import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [*map(int, input().split())]
arr.sort()
for t in product(arr, repeat=M):
    print(*t)
