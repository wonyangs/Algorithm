# Solved on 2022. 1. 20.
# 1717 집합의 표현

import sys
input = sys.stdin.readline

N, M = map(int, input().split())


def findroot(i):
    if tree[i][0] == i:
        return i
    return findroot(tree[i][0])


def union(a, b):
    rootA = findroot(a)
    rootB = findroot(b)
    if rootA == rootB:
        return
    
    if tree[rootA][1] > tree[rootB][1]:
        tree[rootB][0] = rootA
    else:
        tree[rootA][0] = rootB
        tree[rootB][1] += 1


tree = []
for i in range(0, N+1):
    tree.append([i, 0])

for _ in range(M):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        if findroot(a) == findroot(b):
            print("YES")
        else:
            print("NO")
