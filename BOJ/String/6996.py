import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a, b = input().strip().split()
    if Counter(a) == Counter(b):
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
