# Solved on 2022. 6. 5.
# 1015 수열 정렬

N = int(input())
arr = [*map(int, input().split())]
sort_arr = sorted(arr)
res = [-1] * N
for i in range(N):
    for j in range(N):
        if arr[j] == sort_arr[i] and res[j] == -1:
            res[j] = i
            break
print(*res)
