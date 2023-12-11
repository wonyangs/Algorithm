for _ in range(int(input())):
    arr = [*map(int, input().split())]
    res = 0
    res += max(1, arr[0] + arr[4])
    res += 5 * max(1, arr[1] + arr[5])
    res += 2 * max(0, arr[2] + arr[6])
    res += 2 * (arr[3] + arr[7])
    print(res)
