for i in range(1, int(input()) + 1):
    arr = sorted(map(int, input().split()))
    if i != 1:
        print()
    print(f"Scenario #{i}:")
    print("yes" if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2 else "no")
