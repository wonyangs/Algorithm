# Solved on 2022. 6. 23.
# 1275 커피숍2

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


N, Q= map(int, input().split())

arr = [*map(int, input().split())]
height = 2 ** math.ceil(math.log2(N) + 1)
tree = [0] * height
init(0, N - 1, 1)
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    answer = 0
    if x > y:
        query(0, N - 1, 1, y - 1, x - 1)
    else:
        query(0, N - 1, 1, x - 1, y - 1)
    print(answer)
    update(0, N - 1, 1, a - 1, b)
