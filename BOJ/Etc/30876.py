arr = [[*map(int, input().split())] for _ in range(int(input()))]
arr.sort(key=lambda x: x[1])
print(*arr[0])
