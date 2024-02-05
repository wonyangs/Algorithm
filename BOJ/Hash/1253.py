from collections import defaultdict

dic = defaultdict(set)

N = int(input())
arr = [*map(int, input().split())]
arr.sort()
sarr = set(arr)

res = set()
for i in range(N):
    for j in range(i + 1, N):
        if arr[i] + arr[j] not in sarr:
            continue
        dic[arr[i] + arr[j]].add((i, j))

cnt = 0
for i, n in enumerate(arr):
    for a, b in dic[n]:
        if i != a and i != b:
            cnt += 1
            break
print(cnt)
