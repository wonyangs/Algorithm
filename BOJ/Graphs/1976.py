# Solved on 2022. 1. 21.
# 1976 여행 가자

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[*map(int, input().split())] for _ in range(N)]
plan = [*map(int, input().split())]

parent = [i for i in range(N)]
level = [0] * N
def root(n):
    if parent[n] == n:
        return n
    return root(parent[n])


def union(a, b):
    rootA = root(a)
    rootB = root(b)
    if rootA == rootB:
        return
    
    if level[rootA] > level[rootB]:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
        level[rootB] += 1


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union(i, j)

res = []
for n in plan:
    res.append(root(n-1))

canGo = True
for i in res:
    if i != res[0]:
        canGo = False
if canGo:
    print("YES")
else:
    print("NO")
