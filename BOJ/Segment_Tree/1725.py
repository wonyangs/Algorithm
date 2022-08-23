# Solved on 2022. 8. 23.
# 1725 히스토그램

import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def init(start, end, node):
    if start == end:
        tree[node] = start
        return

    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    if arr[tree[node * 2]] <= arr[tree[node * 2 + 1]]:
        tree[node] = tree[node * 2]
    else:
        tree[node] = tree[node * 2 + 1]


def query(start, end, node, lidx, ridx):
    if ridx < start or end < lidx:
        return -1
    if lidx <= start and end <= ridx:
        return tree[node]
    if lidx <= end or start <= ridx:
        mid = (start + end) // 2
        a = query(start, mid, node * 2, lidx, ridx)
        b = query(mid + 1, end, node * 2 + 1, lidx, ridx)
        if a == -1:
            return b
        if b == -1:
            return a
        return a if arr[a] <= arr[b] else b


def res(start, end):
    idx = query(0, N - 1, 1, start, end)
    rng = arr[idx] * (end - start + 1)
    if idx + 1 <= end:
        rng = max(rng, res(idx + 1, end))
    if idx - 1 >= start:
        rng = max(rng, res(start, idx - 1))
    return rng


N = int(input())
arr = [int(input()) for _ in range(N)]
tree = [0] * (2 ** math.ceil(math.log2(N) + 1))
init(0, N - 1, 1)
print(res(0, N - 1))
