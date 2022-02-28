# Solved on 2022. 2. 28.
# 15961 회전 초밥

from collections import defaultdict
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)] * 2

kind = defaultdict(int)
have_c = False
for n in sushi[:k]:
    kind[n] += 1
    if n == c: have_c = True

kind_num = len(kind.keys())
if have_c:
    MAX = kind_num
else:
    MAX = kind_num+1

for i in range(N):
    kind[sushi[i]] -= 1
    kind[sushi[i+k]] += 1
    if sushi[i] == sushi[i+k]:
        continue

    if kind[sushi[i]] == 0:
        kind_num -= 1
        if sushi[i] == c:
            have_c = False
    if kind[sushi[i+k]] == 1:
        kind_num += 1
        if sushi[i+k] == c:
            have_c = True
    if have_c:
        MAX = max(MAX, kind_num)
    else:
        MAX = max(MAX, kind_num+1)

print(MAX)
