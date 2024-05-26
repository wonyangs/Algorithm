N = int(input())
arr = [*map(int, input().split())]
res = [*map(int, input().split())]

cnt = 0
for i in range(N):
    cnt += max(arr[i] - res[i], 0)
print(cnt)
