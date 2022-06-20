# Solved on 2022. 6. 20.
# 23884 알고리즘 수업 - 선택 정렬 4

import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = [*map(int, input().split())]
dic = {}
for i, n in enumerate(arr):
    dic[n] = i
sorted_arr = sorted(arr)

count = 0
for i in range(N-1, -1, -1):
    if sorted_arr[i] != arr[i]:
        count += 1
        idx = dic[sorted_arr[i]]
        arr[i], arr[idx] = arr[idx], arr[i]
        dic[arr[i]] = i
        dic[arr[idx]] = idx
        if count == K:
            print(*arr)
            sys.exit(0)
print(-1)
