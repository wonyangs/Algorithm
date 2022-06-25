# Solved on 2022. 6. 25.
# 18436 수열과 쿼리 37

import math
import sys

input = sys.stdin.readline


def odd_init(start, end, node):
    if start == end:
        odd_tree[node] = arr[start] % 2
        return odd_tree[node]

    mid = (start + end) // 2
    odd_init(start, mid, node * 2)
    odd_init(mid + 1, end, node * 2 + 1)
    odd_tree[node] = odd_tree[node * 2] + odd_tree[node * 2 + 1]


def even_init(start, end, node):
    if start == end:
        even_tree[node] = 1 if arr[start] % 2 == 0 else 0
        return even_tree[node]

    mid = (start + end) // 2
    even_init(start, mid, node * 2)
    even_init(mid + 1, end, node * 2 + 1)
    even_tree[node] = even_tree[node * 2] + even_tree[node * 2 + 1]


def odd_update(start, end, node, idx, value):
    if start == end == idx:
        odd_tree[node] = value % 2
        return odd_tree[node]
    if idx < start or end < idx:
        return 0
    mid = (start + end) // 2
    odd_update(start, mid, node * 2, idx, value)
    odd_update(mid + 1, end, node * 2 + 1, idx, value)
    odd_tree[node] = odd_tree[node * 2] + odd_tree[node * 2 + 1]


def even_update(start, end, node, idx, value):
    if start == end == idx:
        even_tree[node] = 1 if value % 2 == 0 else 0
        return even_tree[node]
    if idx < start or end < idx:
        return 0
    mid = (start + end) // 2
    even_update(start, mid, node * 2, idx, value)
    even_update(mid + 1, end, node * 2 + 1, idx, value)
    even_tree[node] = even_tree[node * 2] + even_tree[node * 2 + 1]


def query(start, end, node, lidx, ridx, tree):
    global answer
    if ridx < start or end < lidx:
        return
    if lidx <= start and end <= ridx:
        answer += tree[node]
        return
    if lidx <= end or start <= ridx:
        mid = (start + end) // 2
        query(start, mid, node * 2, lidx, ridx, tree)
        query(mid + 1, end, node * 2 + 1, lidx, ridx, tree)
        return


N = int(input())
arr = [*map(int, input().split())]
M = int(input())

height = 2 ** math.ceil(math.log2(N) + 1)
odd_tree = [0] * height
even_tree = [0] * height
odd_init(0, N - 1, 1)
even_init(0, N - 1, 1)
for _ in range(M):
    a, b, c = map(int, input().split())

    if a == 1:
        odd_update(0, N - 1, 1, b - 1, c)
        even_update(0, N - 1, 1, b - 1, c)
    elif a == 2:
        answer = 0
        query(0, N - 1, 1, b - 1, c - 1, even_tree)
        print(answer)
    else:
        answer = 0
        query(0, N - 1, 1, b - 1, c - 1, odd_tree)
        print(answer)
