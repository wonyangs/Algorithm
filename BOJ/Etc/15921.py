N = int(input())
if N != 0:
    arr = [*map(int, input().split())]
if N == 0 or sum(arr) == 0:
    print("divide by zero")
else:
    print("1.00")
