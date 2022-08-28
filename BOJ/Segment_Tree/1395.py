# Solved on 2022. 8. 28.
# 1395 스위치

import math
import sys
input = sys.stdin.readline


def lazy_update(start, end, node):
    if lazy[node] == 0:
        return
    tree[node] = (end - start + 1) - tree[node]
    if start != end:
        lazy[node * 2] ^= 1
        lazy[node * 2 + 1] ^= 1
    lazy[node] = 0


def update(start, end, node, lidx, ridx):
    lazy_update(start, end, node)
    if ridx < start or end < lidx:
        return
    if lidx <= start and end <= ridx:
        tree[node] = (end - start + 1) - tree[node]
        if start != end:
            lazy[node * 2] ^= 1
            lazy[node * 2 + 1] ^= 1
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, lidx, ridx)
    update(mid + 1, end, node * 2 + 1, lidx, ridx)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, node, lidx, ridx):
    lazy_update(start, end, node)
    if ridx < start or end < lidx:
        return 0
    if lidx <= start and end <= ridx:
        return tree[node]
    mid = (start + end) // 2
    a = query(start, mid, node * 2, lidx, ridx)
    b = query(mid + 1, end, node * 2 + 1, lidx, ridx)
    return a + b


N, M = map(int, input().split())
tree_size = 2 ** math.ceil(math.log2(N) + 1)
tree = [0] * tree_size
lazy = [0] * tree_size

for _ in range(M):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        update(0, N - 1, 1, a - 1, b - 1)
    else:
        res = query(0, N - 1, 1, a - 1, b - 1)
        print(res)

