N = int(input())
arr = [*map(int, input().split())]

arr.sort(reverse=True)

MAX = 0
for i, n in enumerate(arr):
    MAX = max(MAX, n + i + 1)
print(MAX+1)
