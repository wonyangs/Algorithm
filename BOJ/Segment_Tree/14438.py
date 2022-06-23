# Solved on 2022. 6. 23.
# 14438 수열과 쿼리 17

import math
import sys

input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def query(start, end, node, lidx, ridx):
    if ridx < start or end < lidx:
        return
    if lidx <= start and end <= ridx:
        global MIN
        MIN = min(MIN, tree[node])
        return
    if lidx <= end or start <= ridx:
        mid = (start + end) // 2
        query(start, mid, node * 2, lidx, ridx)
        query(mid + 1, end, node * 2 + 1, lidx, ridx)
        return


def update(start, end, node, idx, value):
    if start == end == idx:
        tree[node] = value
        return tree[node]
    if idx < start or end < idx:
        return 0
    mid = (start + end) // 2
    update(start, mid, node * 2, idx, value)
    update(mid + 1, end, node * 2 + 1, idx, value)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


N = int(input())
arr = [*map(int, input().split())]
M = int(input())

height = 2 ** math.ceil(math.log2(N) + 1)
tree = [0] * height
init(0, N - 1, 1)

for _ in range(M):
    cmd, a, b = map(int, input().split())

    if cmd == 1:
        update(0, N - 1, 1, a - 1, b)
    else:
        MIN = 1000000001
        query(0, N - 1, 1, a - 1, b - 1)
        print(MIN)
