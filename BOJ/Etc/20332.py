input()
arr = [*map(int, input().split())]
if sum(arr) % 3 != 0:
    print("no")
else:
    print("yes")
