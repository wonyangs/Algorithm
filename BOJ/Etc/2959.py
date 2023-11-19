arr = [*map(int, input().split())]
arr.sort()

print(min(arr[0], arr[1]) * min(arr[2], arr[3]))
