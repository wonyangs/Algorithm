N = int(input())
arr = [*map(int, input().split())]
ss = sorted(arr)
res = 0
for i in range(N):
    if arr[i] != ss[i]:
        res += 1
print(res)
