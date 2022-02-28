# Solved on 2022. 2. 28.
# 3078 좋은 친구

from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [len(input().strip()) for _ in range(N)]
name = defaultdict(int)
for i in range(K+1):
    name[arr[i]] += 1
count = 0
for val in name.values():
    if val > 1:
        count += sum([n for n in range(1, val)])

for i in range(N-K-1):
    name[arr[i]] -= 1
    count += name[arr[i+K+1]]
    name[arr[i+K+1]] += 1

print(count)
