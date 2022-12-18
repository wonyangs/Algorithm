import sys
input = sys.stdin.readline

count = 1
while True:
    arr = [*map(int, input().split())]
    if arr[0] == 0 and len(arr) == 1:
        break
    print("Case %d: Sorting... done!"%count)
    count += 1
