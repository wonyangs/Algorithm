N = int(input())
arr = [0] + [int(input()) for _ in range(N)]
res = 0
M = int(input())
for _ in range(M):
    i = int(input())
    res += arr[i]
print(res)
