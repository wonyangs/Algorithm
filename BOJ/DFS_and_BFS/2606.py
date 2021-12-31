# Solved on 2020.12.21
# 2606 바이러스


import sys
input = sys.stdin.readline


def add(S, V, n):
    for i in V[n]:
        if i in S:
            continue
        else:
            S.add(i)
            add(S, V, i)
    return


def main():
    n = int(input())
    m = int(input())
    V = [[] for _ in range(n+1)]
    arr = set()
    arr.add(1)

    for _ in range(m):
        a, b = map(int, input().split())
        V[a].append(b)
        V[b].append(a)

    add(arr, V, 1)

    print(len(arr)-1)


main()
