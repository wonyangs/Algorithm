N, k = map(int, input().split())
arr = [*map(int, input().split())]
arr.sort(reverse=True)
print(arr[k-1])
