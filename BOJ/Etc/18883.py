N, M = map(int, input().split())
cnt = 1
for i in range(1, N + 1):
    arr = []
    for j in range(1, M + 1):
        arr.append(cnt)
        cnt += 1
    print(*arr)
