# Solved on 2021. 09. 15.
# 15657 N과 M (8)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int, input().split()))
array.sort()

tmp = []


def nm(start, array, tmp, count):
    for i in range(start, n):
        tmp.append(array[i])
        if count < m - 1:
            count += 1
            nm(i, array, tmp, count)
            count -= 1
            tmp.pop()
        elif count == m - 1:
            for j in range(m):
                print(tmp[j], end=" ")
            print()
            tmp.pop()


nm(0, array, tmp, 0)
