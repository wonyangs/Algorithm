# Solved on 2020.12.15
# 10828 스택

import sys
input = sys.stdin.readline


def push(L, n):
    L.append(n)
    return L


def isEmpty(L):
    if len(L) == 0:
        return True
    else:
        return False


def pop(L):
    if isEmpty(L):
        print(-1)
        return L
    else:
        print(L[-1])
        return L[:-1]


def size(L):
    print(len(L))
    return


def top(L):
    if isEmpty(L):
        print(-1)
    else:
        print(L[-1])
    return


n = int(input())
L = []
start = time.time()
for i in range(n):
    a = input().split()
    if a[0] == 'push':
        L = push(L, a[1])
    elif a[0] == 'pop':
        L = pop(L)
    elif a[0] == 'size':
        size(L)
    elif a[0] == 'empty':
        if isEmpty(L):
            print('1')
        else:
            print('0')
    else:  # top
        top(L)
