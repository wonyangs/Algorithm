# Solved on 2020.12.14
# 10816 숫자 카드 2


import sys
input = sys.stdin.readline


n = int(input())
a = map(int, input().split())
m = int(input())
b = map(int, input().split())

hashmap = {}

for i in a:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

print(' '.join(str(hashmap[b]) if b in hashmap else '0' for b in b))
