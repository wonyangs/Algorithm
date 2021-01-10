# Solved on 2020.12.17
# 1764 듣보잡


import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    a = set()
    b = set()

    for i in range(n):
        a.add(input().strip())

    for i in range(m):
        b.add(input().strip())

    L = a & b

    print(len(L), sorted(L))
    for i in sorted(L):
        print(i)


main()
