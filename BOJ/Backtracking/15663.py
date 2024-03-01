from itertools import permutations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [*map(int, input().split())]

s = set()
for p in permutations(arr, M):
    s.add(tuple(p))
for t in sorted(s):
    print(*t)
