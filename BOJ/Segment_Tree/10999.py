# Solved on 2022. 8. 25.
# 10999 구간 합 구하기 2

import math
import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def lazy_update(start, end, node):
    if lazy[node] == 0:
        return
    tree[node] += lazy[node] * (end - start + 1)
    if start != end:
        lazy[node * 2] += lazy[node]
        lazy[node * 2 + 1] += lazy[node]
    lazy[node] = 0


def update(start, end, node, lidx, ridx, value):
    lazy_update(start, end, node)
    if ridx < start or end < lidx:
        return
    if lidx <= start and end <= ridx:
        tree[node] += value * (end - start + 1)
        if start != end:
            lazy[node * 2] += value
            lazy[node * 2 + 1] += value
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, lidx, ridx, value)
    update(mid + 1, end, node * 2 + 1, lidx, ridx, value)
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


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree_size = 2 ** math.ceil(math.log2(N) + 1)
tree = [0] * tree_size
lazy = [0] * tree_size
init(0, N - 1, 1)

for _ in range(M + K):
    cmd = [*map(int, input().split())]
    if cmd[0] == 1:
        update(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1, cmd[3])
    else:
        res = query(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1)
        print(res)

