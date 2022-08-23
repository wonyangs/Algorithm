# Solved on 2022. 8. 23.
# 14428 수열과 쿼리 16

import math
import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = (arr[start], start)
        return tree[node]

    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def update(start, end, node, idx, value):
    if start == end == idx:
        tree[node] = (value, idx)
        return tree[node]
    if idx < start or end < idx:
        return (10**9, 10**9)

    mid = (start + end) // 2
    update(start, mid, node * 2, idx, value)
    update(mid + 1, end, node * 2 + 1, idx, value)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def query(start, end, node, lidx, ridx):
    global answer
    if ridx < start or end < lidx:
        return
    if lidx <= start and end <= ridx:
        answer = min(answer, tree[node])
        return
    if lidx <= end or start <= ridx:
        mid = (start + end) // 2
        query(start, mid, node * 2, lidx, ridx)
        query(mid + 1, end, node * 2 + 1, lidx, ridx)
        return


N = int(input())
arr = [*map(int, input().split())]
height = 2 ** math.ceil(math.log2(N) + 1)
M = int(input())
tree = [0] * height
init(0, N - 1, 1)
for _ in range(M):
    answer = (10 ** 9, 10 ** 9)
    cmd = [*map(int, input().split())]
    if cmd[0] == 1:
        update(0, N - 1, 1, cmd[1] - 1, cmd[2])
    else:
        query(0, N - 1, 1, cmd[1] - 1, cmd[2] - 1)
        print(answer[1] + 1)
