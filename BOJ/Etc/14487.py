N = int(input())
arr = [*map(int, input().split())]
print(sum(arr) - max(arr))
