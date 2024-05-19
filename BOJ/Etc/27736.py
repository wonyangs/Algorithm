from math import ceil

N = int(input())
arr = [*map(int, input().split())]
inv = arr.count(0)
if inv >= ceil(N / 2):
    print("INVALID")
else:
    s = sum(arr)
    if s > 0:
        print("APPROVED")
    else:
        print("REJECTED")
