N, M, L = map(int, input().split())
arr = [0] * N
arr[0] = 1

cur = 0
cnt = 0
while max(arr) != M:
    if arr[cur] % 2 == 0:
        cur = (cur - L) % N
    else:
        cur = (cur + L) % N
    arr[cur] += 1
    cnt += 1
print(cnt)
