# Solved on 2022. 8. 23.
# 1517 버블 소트

import math
import sys

input = sys.stdin.readline


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


N = int(input())
arr = sorted((n, i+1) for i, n in enumerate([*map(int, input().split())]))
tree = [0] * (2 ** math.ceil(math.log2(N) + 1))

answer = 0
for _, i in arr:
    query(0, N - 1, 1, i-1, N-1)
    update(0, N - 1, 1, i-1, 1)
print(answer)
