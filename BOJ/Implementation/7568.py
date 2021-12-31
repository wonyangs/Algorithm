# Solved on 2021. 10. 19.
# 7568 덩치

import sys
input = sys.stdin.readline

N = int(input())

people = []
for _ in range(N):
    a, b = map(int, input().split())
    people.append([a, b])

rank = [1] * N
for i in range(N):
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1

for i in rank:
    print(i, end=' ')
print()
