# Solved on 2022. 2. 5.
# 1300 K번째 수

import sys
input = sys.stdin.readline


def binary_search():
    start, end = 1, int(1e9)
    res = 0
    while start <= end:
        mid = (start+end)//2
        hap = 0
        for i in range(1, N+1):
            if mid // i > N:
                hap += N
            else:
                hap += mid//i
                
        if hap < k:
            start = mid + 1
        else:
            end = mid - 1
            res = mid
    return res


N = int(input())
k = int(input())
print(binary_search())
