# Solved on 2022. 6. 23.
# 2268 수들의 합 7

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
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update(start, end, node, idx, value):
    if start == end == idx:
        tree[node] = value
        return tree[node]
    if idx < start or end < idx:
        return 0
    mid = (start + end) // 2
    update(start, mid, node * 2, idx, value)
    update(mid + 1, end, node * 2 + 1, idx, value)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, node, lidx, ridx):
    global answer
    if ridx < start or end < lidx:
        return
    if lidx <= start and end <= ridx:
        answer += tree[node]
        return
    if lidx <= end or start <= ridx:
        mid = (start + end) // 2
        query(start, mid, node * 2, lidx, ridx)
        query(mid + 1, end, node * 2 + 1, lidx, ridx)
        return


N, M = map(int, input().split())

arr = [0] * N
height = 2 ** math.ceil(math.log2(N) + 1)
tree = [0] * height
answer = 0
init(0, N - 1, 1)
for _ in range(M):
    a, b, c = map(int, input().split())

    if a == 1:
        update(0, N - 1, 1, b - 1, c)
    elif a == 0:
        answer = 0
        if b < c:
            query(0, N - 1, 1, b - 1, c - 1)
        else:
            query(0, N - 1, 1, c - 1, b - 1)
        print(answer)
