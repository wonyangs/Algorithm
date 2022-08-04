# Solved on 2022. 8. 4.
# 3151 합이 0

from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]
arr.sort()
cnt_arr = Counter(arr)
res = 0
for i in range(N - 2):
    start, end = i + 1, N - 1
    while start < end:
        if arr[start] + arr[end] + arr[i] == 0:
            if arr[start] == arr[end]:
                res += end - start
            else:
                res += cnt_arr[arr[end]]
            start += 1
        elif arr[start] + arr[end] + arr[i] < 0:
            start += 1
        else:
            end -= 1
print(res)
