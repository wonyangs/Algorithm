N, M = map(int, input().split())
arr1 = [input() for _ in range(N)]
input()
arr2 = [input() for _ in range(N)]

res = 0
for i in range(N):
    for j in range(M):
        if arr1[i][j] == arr2[i][j]:
            res += 1
print(res)
