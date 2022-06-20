# Solved on 2022. 6. 20.
# 23900 알고리즘 수업 - 선택 정렬 6

import sys
input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]
check_arr = [*map(int, input().split())]

dic = {}
diff_idx = set()
for i, n in enumerate(arr):
    dic[n] = i
sorted_arr = sorted(arr)
for i in range(N):
    if check_arr[i] != arr[i]:
        diff_idx.add(i)
if len(diff_idx) == 0:
    print(1)
    sys.exit(0)

count = 0
for i in range(N-1, -1, -1):
    if sorted_arr[i] != arr[i]:
        count += 1
        idx = dic[sorted_arr[i]]
        arr[i], arr[idx] = arr[idx], arr[i]
        dic[arr[i]] = i
        dic[arr[idx]] = idx

        if check_arr[i] == arr[i] and i in diff_idx:
            diff_idx.remove(i)
        if check_arr[i] != arr[i]:
            diff_idx.add(i)
        if check_arr[idx] == arr[idx] and idx in diff_idx:
            diff_idx.remove(idx)
        if check_arr[idx] != arr[idx]:
            diff_idx.add(idx)

        if len(diff_idx) == 0:
            print(1)
            sys.exit(0)
print(0)
