# Solved on 2020.12.22
# 11399 ATM


import heapq
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    total = 0

    q = list(map(int, input().split()))
    heapq.heapify(q)

    for i in range(n, 0, -1):
        total += i * heapq.heappop(q)

    print(total)


main()
