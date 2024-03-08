arr = sorted(map(int, input().split()))

a, b = arr[1] - arr[0], arr[2] - arr[1]

if a == b:
    print(arr[2] + a)
elif a > b:
    print(arr[0] + b)
else:
    print(arr[1] + a)
