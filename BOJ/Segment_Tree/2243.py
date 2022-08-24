# Solved on 2022. 8. 24.
# 2243 사탕상자

import math
import sys

input = sys.stdin.readline


def update(start, end, node, idx, value):
    if start == end == idx:
        tree[node] += value
        return tree[node]
    if idx < start or end < idx:
        return 0
    mid = (start + end) // 2
    update(start, mid, node * 2, idx, value)
    update(mid + 1, end, node * 2 + 1, idx, value)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, node, cnt):
    global res
    if res or cnt < 0:
        return
    if start == end:
        res = start + 1
        return
    mid = (start + end) // 2
    if node * 2 < tree_size and tree[node * 2] >= cnt:
        query(start, mid, node * 2, cnt)
    if node * 2 + 1 < tree_size:
        query(mid + 1, end, node * 2 + 1, cnt - tree[node * 2])
    return


N = int(input())
candy = 1000001
tree_size = 2 ** math.ceil(math.log2(candy) + 1)
tree = [0] * tree_size
for _ in range(N):
    arr = [*map(int, input().split())]

    if arr[0] == 1:
        res = 0
        query(0, candy - 1, 1, arr[1])
        update(0, candy - 1, 1, res - 1, -1)
        print(res)
    else:
        update(0, candy - 1, 1, arr[1] - 1, arr[2])

