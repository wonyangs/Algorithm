for _ in range(int(input())):
    arr = [int(i) for i in input().split() if int(i) % 2 == 0]
    print(sum(arr), min(arr))
