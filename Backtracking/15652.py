# Solved on 2021. 09. 13.
# 15652 N과 M (4)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = []


def nm(count, start, array):
    for i in range(start, n+1):
        array.append(i)
        if count < m-1:
            count += 1
            nm(count, i, array)
            count -= 1
        if count == m-1:
            for j in array:
                print(j, end=" ")
            print()
            array.pop()
        else:
            array.pop()
    return


nm(0, 1, array)
