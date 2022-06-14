# Solved on 2022. 6. 14.
# 10868 최솟값

import math
import sys
input = sys.stdin.readline

def min_init(start, end, node):
    if start == end:
        min_tree[node] = arr[start]
        return min_tree[node]
    
    mid = (start + end) // 2
    min_init(start, mid, node*2)
    min_init(mid+1, end, node*2 + 1)
    min_tree[node] = min(min_tree[node*2], min_tree[node*2 + 1])

def min_query(start, end, node, lidx, ridx):
    if ridx < start or end < lidx:
        return
    if lidx <= start and end <= ridx:
        global MIN
        MIN = min(MIN, min_tree[node])
        return
    if lidx <= end or start <= ridx:
        mid = (start + end) // 2
        min_query(start, mid, node*2, lidx, ridx)
        min_query(mid+1, end, node*2 + 1, lidx, ridx)
        return

N, M = map(int, input().split())

arr = [int(input()) for _ in range(N)]
height = 2 ** math.ceil(math.log2(N) + 1)
min_tree = [0] * height
max_tree = [0] * height
min_init(0, N-1, 1)
MIN = 0

for _ in range(M):
    a, b = map(int, input().split())
    MIN = 1000000001
    min_query(0, N-1, 1, a-1, b-1)
    print(MIN)
