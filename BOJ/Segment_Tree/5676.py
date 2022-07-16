# Solved on 2022. 7. 16.
# 5676 음주 코딩

import math
import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        if arr[start] < 0:
            tree[node] = -1
        elif arr[start] == 0:
            tree[node] = 0
        else:
            tree[node] = 1
        return tree[node]

    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    tree[node] = tree[node * 2] * tree[node * 2 + 1]


def update(start, end, node, idx, value):
    if start == end == idx:
        if value < 0:
            tree[node] = -1
        elif value == 0:
            tree[node] = 0
        else:
            tree[node] = 1
        return tree[node]
    if idx < start or end < idx:
        return 0
    mid = (start + end) // 2
    update(start, mid, node * 2, idx, value)
    update(mid + 1, end, node * 2 + 1, idx, value)
    tree[node] = tree[node * 2] * tree[node * 2 + 1]


def query(start, end, node, lidx, ridx):
    global answer
    if ridx < start or end < lidx:
        return
    if lidx <= start and end <= ridx:
        answer *= tree[node]
        return
    if lidx <= end or start <= ridx:
        mid = (start + end) // 2
        query(start, mid, node * 2, lidx, ridx)
        query(mid + 1, end, node * 2 + 1, lidx, ridx)
        return


while True:
    try:
        N, K = map(int, input().split())
        arr = [*map(int, input().split())]
        height = 2 ** math.ceil(math.log2(N) + 1)
        tree = [0] * height
        init(0, N - 1, 1)
        for _ in range(K):
            cmd, a, b = input().strip().split()
            a, b = int(a), int(b)

            if cmd == 'C':
                update(0, N - 1, 1, a - 1, b)
            else:
                answer = 1
                query(0, N - 1, 1, a - 1, b - 1)
                if answer == 0:
                    print(0, end='')
                elif answer == -1:
                    print('-', end='')
                else:
                    print('+', end='')
        print()
    except Exception:
        break
