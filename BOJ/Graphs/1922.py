# Solved on 2022. 2. 25.
# 1922 네트워크 연결

import heapq
import sys
input = sys.stdin.readline   

def root(n):
    if parent[n] == n:
        return n
    parent[n] = root(parent[n])
    return parent[n]

def union(a, b):
    root_a = root(a)
    root_b = root(b)
    
    if rank[root_a] > rank[root_b]:
        parent[root_b] = parent[root_a]
    else:
        parent[root_a] = parent[root_b]
        rank[root_b] += 1

N = int(input())
M = int(input())
pq = []
for _ in range(M):
    a, b, c = map(int, input().split())
    if a==b:continue
    heapq.heappush(pq, (c, a, b))

res = 0
rank = [1] * (N+1)
parent = [i for i in range(N+1)]
while pq:
    val, a, b = heapq.heappop(pq)
    if root(a) != root(b):
        res += val
        union(a, b)
print(res)
