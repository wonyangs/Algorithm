import sys
from collections import Counter

input = sys.stdin.readline

counter = Counter()
N = int(input())
for _ in range(N):
    s = input().strip()
    counter[s] += 1
print(sorted(counter.most_common(), key=lambda x:(-x[1], x[0]))[0][0])
