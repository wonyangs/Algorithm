# Solved on 2021. 12. 03.
# 4386 별자리 만들기

import sys
input = sys.stdin.readline

N = int(input())
star = []
for _ in range(N):
    a, b = map(float, input().split())
    star.append((a, b))
dist = [[-1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        x = abs(star[j][1] -star[i][1]) ** 2
        y = abs(star[j][0] -star[i][0]) ** 2
        dist[i][j] = (x + y) ** 0.5

parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v, u):
    root1 = find(v)
    root2 = find(u)
    
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal():
    for v in range(N):
        make_set(v)

    mst = []
    edges = []
    for i in range(N):
        for j in range(N):
            edges.append((dist[i][j], i, j))
    edges.sort()
    
    for edge in edges:
        weight, v, u = edge
        if find(v) != find(u):
            union(u, v)
            mst.append(weight)
    return mst


print(round(sum(kruskal()), 2))
