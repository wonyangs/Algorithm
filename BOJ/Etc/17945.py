b, c = map(int, input().split())
arr = sorted([int(-b + (b ** 2 - c) ** 0.5), int(-b - (b ** 2 - c) ** 0.5)])
if arr[0] == arr[1]:
    print(arr[0])
else:
    print(*arr)
