N = int(input())
arr = [*map(int, input().split())]

cnt, res = 0, 0
for i in range(N):
    if arr[i] == 1:
        cnt += 1
    else:
        cnt -= 1
    res += cnt
print(res)
