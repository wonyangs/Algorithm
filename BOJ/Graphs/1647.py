# Solved on 2021. 12. 10.
# 1647 도시 분할 계획

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()

parent = {}
rank = {}
def initNode(n):
    parent[n] = n
    rank[n] = 0

def root(n):
    if parent[n] == n:
        return n
    else:
        parent[n] = root(parent[n])
        return parent[n]

def union(a, b):
    rootA = root(a)
    rootB = root(b)
    if rootA == rootB:
        return False
    else:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB
            rank[rootB] += 1
        return True

def kruskal():
    res = []
    for i in range(1, N+1):
        initNode(i)
    for value, a, b in graph:
        if union(a, b):
            res.append(value)
    return res

res = kruskal()
print(sum(res[:-1]))
