a, b = map(int, input().split())
arr = [a+b, a-b]
print(*sorted(arr, reverse=True))
