while True:
    arr = [*map(int, input().split())]
    if arr[0] == 0:
        break

    N, arr = arr[0], arr[1:]
    res = 1
    for i in range(N):
        a, b = i * 2, i * 2 + 1
        res = res * arr[a] - arr[b]
    print(res)
