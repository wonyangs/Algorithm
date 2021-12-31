# Solved on 2021. 12. 04.
# 1197 최소 스패닝 트리

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b, weight = map(int, input().split())
    edges.append((weight, a, b))

parent = {}
level = {}

# 각 노드를 개별적인 집합으로 만들기
def initNode(v):
    parent[v] = v
    level[v] = 0

# 루트 반환
def searchRoot(v):
    if parent[v] != v:
        parent[v] = searchRoot(parent[v])
    return parent[v]

# 노드 병합
def union(a, b):
    root1 = searchRoot(a)
    root2 = searchRoot(b)
    if root1 == root2:
        return False

    if level[root1] > level[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        
        if level[root1] == level[root2]:
            level[root2] += 1
    return True

# 크루스칼 알고리즘 실행
def kruskal():
    res = 0
    for i in range(1, V+1):
        initNode(i)

    # 간선정보 정렬
        edges.sort()

    for edge in edges:
        weight, a, b = edge
        if union(a, b):
            res += weight
    return res

print(kruskal())
